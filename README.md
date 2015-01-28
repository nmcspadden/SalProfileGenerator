SalProfileGenerator
======

Simple Python script that uses [Tim Sutton's mcxToProfile script](https://github.com/timsutton/mcxToProfile) to generate a .mobileconfig profile that can be installed on [Sal](https://github.com/salsoftware/sal) clients, with the machine key and URL.

These scripts must be run from the Sal host, and are designed to work with the [Sal Docker image](https://registry.hub.docker.com/u/macadmins/sal/), as it assumes Sal is installed in `/home/docker/sal/`.

To use:
---

The script takes one required argument, one optional argument.  

The Machine Group key is required, and is generated in Sal by making a new Machine Group within a Business Unit.

The Server URL is optional, and can be specified with either `-u` or `--url`.  The URL defaults to [http://sal](http://sal).

`./generate_sal_profile.py <key> --url <URL>`

Examples:

`./generate_sal_profile.py yym5fuwllm2eaqucxkwzbelji81ewfs5zgxy8qyj5ytzmsheqptpd1u564z0wuv1sqokd8uhi31j2b6wnfv4kasqv4jsmujmv24jiyn8chjt538751mwhia4oyaa5nzb`

`./generate_sal_profile.py yym5fuwllm2eaqucxkwzbelji81ewfs5zgxy8qyj5ytzmsheqptpd1u564z0wuv1sqokd8uhi31j2b6wnfv4kasqv4jsmujmv24jiyn8chjt538751mwhia4oyaa5nzb --url http://sal.domain.com`

Generating all profiles:
----
This also includes a handy script for generating profiles for all current machine keys.  Just run the generate_all_profiles.sh script:  
`./generate_all_profiles.sh`

It will create a com.salsoftware.sal.<key>.mobileconfig, where <key> is the first five characters of the Machine Group key.

Example:  
`./generate_all_profile.sh`    
Then look:  
`ls -l | grep com.salsoftware.sal`  
Result:  
`root@e5c8f459da53:/SalProfileGenerator# ls -l | grep com.salsoftware.sal`  
`-rw-r--r--. 1 root root  1748 Jan 28 22:10 com.salsoftware.sal.bhan5.mobileconfig`  
`-rw-r--r--. 1 root root  1748 Jan 28 22:10 com.salsoftware.sal.cf1hg.mobileconfig`

If using this with the Sal Docker image, you can then use `docker cp` to copy them off the Sal container to the Docker host, and deploy them.