SalProfileGenerator
======

Simple Python script that uses [Tim Sutton's mcxToProfile script](https://github.com/timsutton/mcxToProfile) to generate a .mobileconfig profile that can be installed on [Sal](https://github.com/salsoftware/sal) clients, with the machine key and URL.

These scripts must be run from the Sal host, and are designed to work with the [Sal Docker image](https://registry.hub.docker.com/u/macadmins/sal/), as it assumes Sal is installed in `/home/docker/sal/`.

Two scripts are included - a Python script to generate an individual profile, and a Bash shell script to generate all profiles for all Machine Group keys.

To use:
---

The Python generate_sal_profile.py script takes the following arguments:  

*	`key` - The Machine Group key is **required**, and is generated in Sal by making a new Machine Group within a Business Unit.
*	`url` - The Server URL is **optional**, and can be specified with either `-u` or `--url`.  The URL defaults to [http://sal](http://sal).
*	`output` - Output path is **optional**, and can be specified with either `-o` or `--output`.  This can be either a folder to put profiles in, or a specific filename. The default path is `com.salsoftware.sal.mobileconfig` in the current working directory.

`./generate_sal_profile.py <key> --url <URL>`

Examples:

`./generate_sal_profile.py yym5fuwllm2eaqucxkwzbelji81ewfs5zgxy8qyj5ytzmsheqptpd1u564z0wuv1sqokd8uhi31j2b6wnfv4kasqv4jsmujmv24jiyn8chjt538751mwhia4oyaa5nzb`

`./generate_sal_profile.py yym5fuwllm2eaqucxkwzbelji81ewfs5zgxy8qyj5ytzmsheqptpd1u564z0wuv1sqokd8uhi31j2b6wnfv4kasqv4jsmujmv24jiyn8chjt538751mwhia4oyaa5nzb --url http://sal.domain.com`

`./generate_sal_profile.py yym5fuwllm2eaqucxkwzbelji81ewfs5zgxy8qyj5ytzmsheqptpd1u564z0wuv1sqokd8uhi31j2b6wnfv4kasqv4jsmujmv24jiyn8chjt538751mwhia4oyaa5nzb --url http://sal.domain.com --output ~/Desktop/profiles/`

`./generate_sal_profile.py yym5fuwllm2eaqucxkwzbelji81ewfs5zgxy8qyj5ytzmsheqptpd1u564z0wuv1sqokd8uhi31j2b6wnfv4kasqv4jsmujmv24jiyn8chjt538751mwhia4oyaa5nzb --url http://sal.domain.com --output ~/Desktop/profiles/com.salsoftware.sal.MachineGroupA.mobileconfig`

Generating all profiles:
----
This also includes a handy script for generating profiles for all current Machine Group keys.  Just run the generate_all_profiles.sh script:  
`./generate_all_profiles.sh`

If you wish to generate your profiles using a different URL from the default, pass it in as the shell argument:
`./generate_all_profiles.sh "http://sal.domain.com"`

It will create a com.salsoftware.sal.\<key\>.mobileconfig, where \<key\> is the first five characters of the Machine Group key.

Example:  
`./generate_all_profile.sh`    
Then look:  
`ls -l | grep com.salsoftware.sal`  
Result:  
`root@e5c8f459da53:/SalProfileGenerator# ls -l | grep com.salsoftware.sal`  
`-rw-r--r--. 1 root root  1748 Jan 28 22:10 com.salsoftware.sal.bhan5.mobileconfig`  
`-rw-r--r--. 1 root root  1748 Jan 28 22:10 com.salsoftware.sal.cf1hg.mobileconfig`

Using this with Docker:
----

You can either use the automated build for [Sal-Profiles](https://registry.hub.docker.com/u/nmcspadden/sal-profiles/), which is Sal with this script incorporated, or you can add it to your Sal containers manually.  

If you're adding this to an existing Sal container, follow these steps:

Clone the repo: 

`docker exec sal git clone https://github.com/nmcspadden/SalProfileGenerator.git /usr/local/salprofilegenerator`  

Since the container's already running, we can't add an environmental variable for PROFILE_PATH.  You'll need to create the default output path::  
`docker exec sal mkdir -p /home/docker/profiles` 

Then, execute the script:  
`docker exec sal /usr/local/salprofilegenerator/generate_all_profiles.sh`

Copy the created profiles out:
`docker cp sal:/home/docker/profiles /path/to/profiles/folder/on/Docker/host/`