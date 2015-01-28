SalProfileGenerator
======

Simple Python script that uses [Tim Sutton's mcxToProfile script](https://github.com/timsutton/mcxToProfile) to generate a .mobileconfig profile that can be installed on [Sal](https://github.com/salsoftware/sal) clients, with the machine key and URL.

To use:
---

The script takes one required argument, one optional argument.  

The Machine Group key is required, and is generated in Sal by making a new Machine Group within a Business Unit.

The Server URL is optional, and can be specified with either `-u` or `--url`.  The URL defaults to [http://sal](http://sal).

`./generate_sal_profile.py <key> --url <URL>`

Examples:

`./generate_sal_profile.py yym5fuwllm2eaqucxkwzbelji81ewfs5zgxy8qyj5ytzmsheqptpd1u564z0wuv1sqokd8uhi31j2b6wnfv4kasqv4jsmujmv24jiyn8chjt538751mwhia4oyaa5nzb`

`./generate_sal_profile.py yym5fuwllm2eaqucxkwzbelji81ewfs5zgxy8qyj5ytzmsheqptpd1u564z0wuv1sqokd8uhi31j2b6wnfv4kasqv4jsmujmv24jiyn8chjt538751mwhia4oyaa5nzb http://sal.domain.com`