{
    "targets": [{
        "target_name": "module",
        "sources": [ "src/module.cc", "src/functions.cc"],
        "include_dirs" : [
            "<!(node -e \"require('nan')\")"
        ],
        "win_delay_load_hook": "false",
        "msvs_settings": {

        },
        "msbuild_settings": {

        },            
        "defines":["UNICODE","_UNICODE"]
    }]
}