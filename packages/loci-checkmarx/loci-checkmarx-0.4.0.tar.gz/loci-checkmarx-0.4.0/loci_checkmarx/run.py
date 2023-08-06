import click
import os
from rich.progress import Progress
import loci_checkmarx.utils as lcu


@click.command()
@click.option("-f", "--input-file",
              prompt="Checkmarx XML file",
              help="The Checkmarx XML file with the output of a scan",
              required=True,
              type=str)
@click.option("-i", "--imports",
              help="Specific vulnerabilities or severities (comma separated) to import",
              required=True,
              type=str,
              default="")
def run(input_file, imports):
    """Process a Checkmarx XML file and add results to Loci Notes"""

    lcu.print_info("Getting directory project information...")
    project_id, project_name = lcu.get_project_id_from_config_in_dir(os.getcwd())
    if project_id is None or project_name is None:
        lcu.print_error("Unable to determine associated project. To correct this, run this under a directory "
                        "associated with a Loci Notes project.")
        quit(-1)
    lcu.print_success(f"Using [bold]{project_name}[/bold].")

    # This check is because importing CM results takes FOREVER if you don't limit what get pulled in..
    if imports is None or imports.strip() == "":
        lcu.print_error("A vulnerability or severity to import was not given. Importing entire files "
                        "is not supported as this can take hours even for smaller result sets.")
        quit(-1)

    results_list = lcu.open_results_file_and_get_results(input_file)

    imports_list = imports.split(",")

    for i in range(len(imports_list)):
        # Remove whitespace, lowercase all, remove underscores
        imports_list[i] = imports_list[i].strip().lower().replace("_", " ")

    imported_severities_list = []
    if "high" in imports_list:
        imported_severities_list.append("high")
    if "medium" in imports_list:
        imported_severities_list.append("medium")
    if "low" in imports_list:
        imported_severities_list.append("low")
    if "info" in imports_list or "information" in imports_list or "informational" in imports_list:
        imported_severities_list.append("information")

    # First count up total number of results to get a semi-accurate count of the results for the progress bar
    valid_results_found = 0
    for result in results_list:
        if result.query_name.lower() in imports_list or result.severity.lower() in imported_severities_list:
            valid_results_found += 1

    if valid_results_found == 0:
        lcu.print_error("No results were found for the given imports. See the [bold]summary[/bold]"
                        " for valid vulnerabilities, or use 'High', 'Medium', 'Low', and 'Info' "
                        "to import by severity.")
        quit(-1)

    with Progress() as progress_bar:
        task = progress_bar.add_task(f"Importing {valid_results_found} results...", total=valid_results_found)

        for result in results_list:
            if result.query_name.lower() in imports_list or result.severity.lower() in imported_severities_list:

                # In the future, we can probably ask the user if they want to add a note for EVERY
                # node along the path, but for now we just add the top and bottom path nodes, and
                # everything in between is implicit.

                # The top node appears to always match the Result file and line, but I'm not sure if
                # it always does. If not, fix it here.
                # Additionally, it appears that each Result only ever has one Path.

                # Send the info to the LN server for the top (source) node
                new_note = {}
                new_note["artifact_descriptor"] = result.get_src_artifact()
                new_note["submission_tool"] = "Checkmarx"
                new_note["note_type"] = "LOG"
                new_note["contents"] = "**Source for Security Issue**\n\n"
                new_note["contents"] += "**Description** - " + result.query_name + "\n"
                new_note["contents"] += "**Severity** - " + result.severity.capitalize()

                # Detection and prevention of duplicate notes is handled by the server.
                lcu.loci_api_req(f"/api/projects/{project_id}/notes", method="POST",
                                 data=new_note, show_loading=False)

                # Send the info to the LN server for the bottom (sink) node
                new_note = {}
                new_note["artifact_descriptor"] = result.get_sink_artifact()
                new_note["submission_tool"] = "Checkmarx"
                new_note["note_type"] = "LOG"
                new_note["contents"] = "**Sink for Security Issue**" + "\n"
                new_note["contents"] += "**Description** - " + result.query_name + "\n"
                new_note["contents"] += "**Severity** - " + result.severity.capitalize()

                # Detection and prevention of duplicate notes is handled by the server.
                lcu.loci_api_req(f"/api/projects/{project_id}/notes", method="POST",
                                 data=new_note, show_loading=False)

                # Next, link the two artifacts. The server will automatically add a link in each
                # direction with a single call, so we only need to send one request.
                new_note = {}
                new_note["artifact_descriptor"] = result.get_src_artifact()
                new_note["submission_tool"] = "Checkmarx"
                new_note["note_type"] = "LINK"
                new_note["contents"] = result.get_sink_artifact()

                # Detection and prevention of duplicate notes is handled by the server.
                lcu.loci_api_req(f"/api/projects/{project_id}/notes", method="POST",
                                 data=new_note, show_loading=False)

                progress_bar.update(task, advance=1)
