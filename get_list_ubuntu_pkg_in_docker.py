import docker

local_shared_dir = '/Volumes/backup_disk/clarity/clarity_automation_test/ubuntu/'
docker_shared_dir = '/download_pkg/'
container_name = 'ubuntu_download_pkg'

package = 'junit'
version = '3.8.2-9'



client = docker.from_env()
container = client.containers.get(container_name)
print(container)
down_pkg = container.exec_run("apt-get download " + package + "=" + version, workdir=docker_shared_dir, stdout=True, stdin=True)
if down_pkg.exit_code != 0:
    print('It is not exsist')
    pass
else:
    # b = container.exec_run("ls " + package + "*" + version + "*", workdir='/download_pkg', stdout=True, stdin=False)
    command = 'ls ' + package + '*' + version + '*'
    f_file = container.exec_run("/bin/bash -c '" + command + "'", workdir=docker_shared_dir, stdout=True, stdin=False)
    output_v = f_file.output.decode("utf-8")
    file_name = output_v.replace('\n', '')
    file_location = local_shared_dir + file_name
    print(file_location)
