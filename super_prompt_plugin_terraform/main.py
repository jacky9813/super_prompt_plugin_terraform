import typing
import logging
import glob
import os

import super_prompt.types

TF_SYMBOL = "T"

logger = logging.getLogger("super_prompt_plugin_terraform")


def main(config: dict) -> typing.Optional[super_prompt.types.PluginResponse]:
    if len(glob.glob("*.tf")) == 0 and len(glob.glob("*.tf.json")) == 0:
        return
    
    workspace_name = "default"
    if os.path.exists(".terraform/environment"):
        with open(".terraform/environment", mode="r") as tf_env_fd:
            workspace_name = tf_env_fd.read().strip()

    
    return super_prompt.types.PluginResponse(
        TF_SYMBOL,
        workspace_name,
        [0x7B, 0x42, 0xBC]
    )


if __name__ == "__main__":
    print(main({}))

