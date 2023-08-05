from nornir.core.task import Task, Result

from netbox_network_importer.pyats.parser import show_interfaces, show_vlan, show_interfaces_status, show_interfaces_trunk
from netbox_network_importer.data_converter.network_to_netbox import convert_interfaces, convert_lag_interfaces, convert_interfaces_ips, convert_interfaces_vlans_iosxr, convert_interfaces_vlans_iosxe
from netbox_network_importer.helper import is_interface_lag, get_address_from_netbox_task

from netbox_network_importer.netbox_updater.interfaces import process_interfaces
from netbox_network_importer.netbox_updater.lag_interfaces import process_lag_interfaces
from netbox_network_importer.netbox_updater.interfaces_ips import process_interfaces_ips
from netbox_network_importer.netbox_updater.interfaces_vlans import process_interfaces_vlans
from netbox_network_importer.netbox_updater.facts import process_facts

from netbox_network_importer.results.results import TaskNetboxResult, Status

from netbox_network_importer.connections.Napalm import Napalm


def synchronize_serials(task: Task, pyats) -> Result:
    # Parse interfaces information from network
    try:
        host_ip = get_address_from_netbox_task(task)
        dev = Napalm(host_ip, task.host.platform)
        napalm_facts = dev.get_facts()
    except Exception as e:
        task_result = TaskNetboxResult(task=task.name,
                                       netbox_results=[],
                                       status="failed",
                                       exception=e,
                                       comment="Failed to get facts data")
        return Result(
            host=task.host,
            exception=e,
            result=f"{task.host.name} - Failed to get facts data via Napalm",
            failed=True,
            netbox_results=task_result,
            diff=task_result.to_dict(except_status_codes=[Status.NOT_CHANGED]))

    # CRUD operations on Netbox with received data
    nb_results_list = process_facts(host=task.host,
                                    napalm_facts=napalm_facts)

    task_result = TaskNetboxResult(task=task.name,
                                   netbox_results=nb_results_list,
                                   status="completed")
    return Result(host=task.host,
                  result="Facts were processed",
                  netbox_results=task_result,
                  diff=task_result.to_dict(except_status_codes=[Status.NOT_CHANGED]))


def synchronize_interfaces(task: Task, pyats) -> Result:
    """Sync interfaces of device between network and Netbox.

    List of tasks that poll data from the network (via PyAts with genie parser),
    process it into the required form (converts data to netbox friendly params),
    executes the CRUD action on Netbox

    :param pyats: passed pyats connection instance with loaded testbed
    """

    # Parse interfaces information from network
    try:
        host_ip = get_address_from_netbox_task(task)
        dev = Napalm(host_ip, task.host.platform)
        napalm_interfaces = dev.get_interfaces()
    except Exception as e:
        task_result = TaskNetboxResult(task=task.name,
                                       netbox_results=[],
                                       status="failed",
                                       exception=e,
                                       comment="Failed to get interfaces data")
        return Result(
            host=task.host,
            exception=e,
            result=f"{task.host.name} - Failed to get interfaces data via Napalm",
            failed=True,
            netbox_results=task_result,
            diff=task_result.to_dict(except_status_codes=[Status.NOT_CHANGED]))

    # Convert parsed information to Netbox friendly data (fields)
    converted_ifcs = convert_interfaces(napalm_interfaces=napalm_interfaces)

    # CRUD operations on Netbox with received data
    nb_results_list = process_interfaces(host=task.host,
                                         parsed_interfaces=converted_ifcs)

    task_result = TaskNetboxResult(task=task.name,
                                   netbox_results=nb_results_list,
                                   status="completed")
    return Result(host=task.host,
                  result="Interfaces were processed",
                  netbox_results=task_result,
                  diff=task_result.to_dict(except_status_codes=[Status.NOT_CHANGED]))


def synchronize_interfaces_lags(task: Task, pyats) -> Result:
    """Sync lags of device between network and Netbox.

    List of tasks that poll data from the network (via PyAts with genie parser),
    process it into the required form (converts data to netbox friendly params),
    executes the CRUD action on Netbox

    :param pyats: passed pyats connection instance with loaded testbed
    """

    try:
        genie_interfaces = show_interfaces(pyats=pyats,
                                           hostname=task.host.name)
    except Exception as e:
        task_result = TaskNetboxResult(task=task.name,
                                       netbox_results=[],
                                       status="failed",
                                       exception=e,
                                       comment="Unable to parse show_interfaces via PyATS")
        return Result(
            host=task.host,
            exception=e,
            result=f"{task.host.name} - Unable to parse show_interfaces via PyATS",
            netbox_results=task_result,
            diff=task_result.to_dict(except_status_codes=[Status.NOT_CHANGED]),
            failed=True)

    # Filter lag interfaces
    genie_lag_interfaces = {
        key: value for key, value in genie_interfaces.items() if is_interface_lag(key)}

    # Convert parsed information to Netbox friendly data (fields)
    converted_lag_ifcs = convert_lag_interfaces(genie_lag_interfaces=genie_lag_interfaces,
                                                platform=task.host.platform)
    # CRUD operations on Netbox with received data
    nb_results_list = process_lag_interfaces(host=task.host,
                                             parsed_lag_interfaces=converted_lag_ifcs)

    status = "no_data_parsed" if not converted_lag_ifcs else "completed"
    result = "No lags were parsed" if not converted_lag_ifcs else "LAGS were processed"

    task_result = TaskNetboxResult(task.name,
                                   nb_results_list,
                                   status=status)

    return Result(host=task.host,
                  result=result,
                  netbox_results=task_result,
                  diff=task_result.to_dict(except_status_codes=[Status.NOT_CHANGED]))


def synchronize_interfaces_ips(task: Task, pyats) -> Result:
    """Sync interfaces IP addresses of device between network and Netbox.

    List of tasks that poll data from the network (via PyAts with genie parser),
    process it into the required form (converts data to netbox friendly params),
    executes the CRUD action on Netbox
    """

    try:
        host_ip = get_address_from_netbox_task(task)
        dev = Napalm(host_ip, task.host.platform)
        napalm_interfaces_ip = dev.get_interfaces_ip()
    except Exception as e:
        task_result = TaskNetboxResult(task=task.name,
                                       netbox_results=[],
                                       status="failed",
                                       exception=e,
                                       comment="Failed to get interfaces ip info Napalm")
        return Result(
            host=task.host,
            exception=e,
            result=f"{task.host.name} - Failed to get interfaces ip info Napalm",
            failed=True,
            netbox_results=task_result,
            diff=task_result.to_dict(except_status_codes=[Status.NOT_CHANGED]))

    # parse ips them
    converted_ifcs = convert_interfaces_ips(napalm_interfaces_ip=napalm_interfaces_ip,
                                            platform=task.host.platform)

    # CRUD operations on Netbox with received data
    nb_results_list = process_interfaces_ips(host=task.host,
                                             parsed_interfaces=converted_ifcs)

    task_result = TaskNetboxResult(task=task.name,
                                   netbox_results=nb_results_list,
                                   status="completed")

    return Result(host=task.host,
                  result="IPs were processed",
                  netbox_results=task_result,
                  diff=task_result.to_dict(except_status_codes=[
                                           Status.NOT_CHANGED]),
                  status="completed")


def synchronize_interfaces_vlans(task: Task, pyats) -> Result:
    # Parse interfaces information from network

    try:
        if task.host.platform == 'iosxr':
            task_result = TaskNetboxResult(task.name,
                                           [],
                                           status="IOSXR - SKIPPED")
            return Result(
                host=task.host,
                result=f"{task.host.name} {task.host.platform} - Skipping IOSXR vlans synchronization",
                failed=False,
                netbox_results=task_result,
                diff={})

        elif task.host.platform == 'iosxe' or task.host.platform == 'ios':
            vlans = show_vlan(pyats=pyats, hostname=task.host.name)
            vlans_interfaces = show_interfaces_status(
                pyats=pyats, hostname=task.host.name)
            trunks = show_interfaces_trunk(
                pyats=pyats, hostname=task.host.name)

            RESULT = convert_interfaces_vlans_iosxe(
                vlans, vlans_interfaces, trunks)
        else:
            raise NotImplementedError
    except Exception as e:
        task_result = TaskNetboxResult(task=task.name,
                                       netbox_results=[],
                                       status="failed",
                                       exception=e,
                                       comment=f"{task.host.name} {task.host.platform}- Failed to get/parse vlan information")
        return Result(
            host=task.host,
            exception=e,
            result=f"{task.host.name} {task.host.platform}- Failed to get/parse vlan information",
            failed=True,
            netbox_results=task_result,
            diff=task_result.to_dict(except_status_codes=[Status.NOT_CHANGED]))

    # CRUD operations on Netbox with received data
    nb_results_list = process_interfaces_vlans(
        host=task.host, parsed_data=RESULT)

    task_result = TaskNetboxResult(task.name,
                                   nb_results_list,
                                   status="completed")

    # TODO:
    failed = False
    if task_result.to_dict().get(task.name).get('results', {}).get("EXCEPTION"):
        failed = True
        task_result.status = "FAILED"

    changed = False
    if task_result.to_dict().get(task.name).get('results', {}).get("CHANGED"):
        changed = True

    diff = task_result.to_dict(except_status_codes=[Status.NOT_CHANGED])
    return Result(host=task.host,
                  result="VLANS were processed",
                  netbox_results=task_result,
                  diff=diff,
                  failed=failed,
                  changed=changed)
