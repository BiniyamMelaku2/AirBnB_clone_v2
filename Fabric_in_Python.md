

## Resources
Read or watch:

* [How to use Fabric](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)
* [How to use Fabric in Python](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python?__cf_chl_managed_tk__=pmd_4qldcZQsF3PenyVFKzZRkTkcJ3lJB0WFYbFf3YzmbKk-1629884937-0-gqNtZGzNAvujcnBszQm9)
* [Fabric and command line options](https://docs.fabfile.org/en/1.13/usage/fab.html)
* [Nginx configuration for beginners](http://nginx.org/en/docs/beginners_guide.html)
* [Difference between root and alias on NGINX](https://blog.heitorsilva.com/en/nginx/diferenca-entre-root-e-alias-do-nginx/)
* [Fabric for Python 3](https://github.com/mathiasertl/fabric)
* [Fabric Documentation](http://www.fabfile.org/)
* [Fabric – Automate Your Linux Administration Tasks and Application Deployments Over SSH](https://www.tecmint.com/automating-linux-system-administration-tasks/)
* [Python Fabric: How to answer to keyboard input](https://stackoverflow.com/questions/2246256/python-fabric-how-to-answer-to-keyboard-input#2246416)
* [Automate your deployment and SSH activities with Fabric](https://medium.com/python-pandemonium/automate-your-deployment-and-ssh-activities-with-fabric-e59e0db17537)
* [Python fabric.api Module](https://www.programcreek.com/python/index/1206/fabric.api)

## Tasks

## [0. Prepare your web servers](./0-setup_web_static.sh)
Write a Bash script that sets up your web servers for the deployment of web_static. It must:

* Install Nginx if it not already installed
* Create the folder /data/ if it doesn’t already exist
* Create the folder /data/web_static/ if it doesn’t already exist
* Create the folder /data/web_static/releases/ if it doesn’t already exist
* Create the folder /data/web_static/shared/ if it doesn’t already exist
* Create the folder /data/web_static/releases/test/ if it doesn’t already exist
* Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
* Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
* Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
* Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:

    Use alias inside your Nginx configuration
    [Tip](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)

  Your program should always exit successfully. Don’t forget to run your script on both of your web servers.

```
ubuntu@89-web-01:~/$ sudo ./0-setup_web_static.sh
ubuntu@89-web-01:~/$ echo $?
0
ubuntu@89-web-01:~/$ ls -l /data
total 4
drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
ubuntu@89-web-01:~/$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 ubuntu ubuntu   30 Mar 7 22:30 current -> /data/web_static/releases/test
drwxr-xr-x 3 ubuntu ubuntu 4096 Mar 7 22:29 releases
drwxr-xr-x 2 ubuntu ubuntu 4096 Mar 7 22:29 shared
ubuntu@89-web-01:~/$ ls /data/web_static/current
index.html
ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ 
```
  

## [1. Compress before sending](./1-pack_web_static.py)
Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

* Prototype: [def do_pack():]
* All files in the folder web_static must be added to the final archive
* All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
* The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
* The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return None
```
@ubuntu:~/AirBnB_clone_v2$ fab -f 1-pack_web_static.py do_pack 
Packing web_static to versions/web_static_20170314233357.tgz
[localhost] local: tar -cvzf versions/web_static_20170314233357.tgz web_static
web_static/
web_static/.DS_Store
....
Done.
@ubuntu:~/AirBnB_clone_v2$ ls -l versions/web_static_20170314233357.tgz
-rw-rw-r-- 1 ubuntu ubuntu 21283 Mar 14 23:33 versions/web_static_20170314233357.tgz
@ubuntu:~/AirBnB_clone_v2$
```

## [2. Deploy archive!](./2-do_deploy_web_static.py)
Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy:

* Prototype: [def do_deploy(archive_path):]
* Returns False if the file at the path archive_path doesn’t exist
* The script should take the following steps:
```
 o Upload the archive to the /tmp/ directory of the web server
 o Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
 o Delete the archive from the web server
 o Delete the symbolic link /data/web_static/current from the web server
 o Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
```
* All remote commands must be executed on your both web servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
* Returns True if all operations have been done correctly, otherwise returns False
* You must use this script to deploy it on your servers: xx-web-01 and xx-web-02

Disclaimer: commands execute by Fabric displayed below are linked to the way we implemented the archive function do_pack - like the mv command - depending of your implementation of it, you may don’t need it
```
@ubuntu:~/AirBnB_clone_v2$ fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz -i my_ssh_private_key -u ubuntu
[52.55.249.213] Executing task 'do_deploy'
[52.55.249.213] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
[52.55.249.213] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: rm /tmp/web_static_20170315003959.tgz
[52.55.249.213] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
[52.55.249.213] run: rm -rf /data/web_static/current
[52.55.249.213] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
New version deployed!
[54.157.32.137] Executing task 'deploy'
[54.157.32.137] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
[54.157.32.137] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: rm /tmp/web_static_20170315003959.tgz
[54.157.32.137] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
[54.157.32.137] run: rm -rf /data/web_static/current
[54.157.32.137] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
New version deployed!

Done.
Disconnecting from 54.157.32.137... done.
Disconnecting from 52.55.249.213... done.
@ubuntu:~/AirBnB_clone_v2$ 
@ubuntu:~/AirBnB_clone_v2$ curl 54.157.32.137/hbnb_static/0-index.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AirBnB clone</title>
    </head>
    <body style="margin: 0px; padding: 0px;">
        <header style="height: 70px; width: 100%; background-color: #FF0000">
        </header>

        <footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
            <p style="line-height: 60px; margin: 0px;">Holberton School</p>
        </footer>
    </body>
</html>
@ubuntu:~/AirBnB_clone_v2$ 
```

mv web_static_20210826125203.tgz /tmp/web_static_20210826125203.tgz
sudo mkdir -p /data/web_static/releases/file_wo_ext
sudo tar -xzf /tmp/web_static_20210826125203.tgz -C /data/web_static/releases/file_wo_ext/
sudo mv /data/web_static/releases/file_wo_ext/web_static/* /data/web_static/releases/file_wo_ext/
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/file_wo_ext/ /data/web_static/current
sudo rm -rf /data/web_static/releases/file_wo_ext/web_static
sudo rm /tmp/web_static_20210826125203.tgz
ls /data/web_static/releases/file_wo_ext/
curl 34.139.184.21/hbnb_static/0-index.html

server_name biniyammelaku.tech www.biniyammelaku.tech web-01.biniyammelaku.tech web-02.biniyammelaku.tech lb-01.biniyammelaku.tech;

