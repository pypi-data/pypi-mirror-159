"""command message."""
import shutil
from typing import Tuple

import click

from funpinpin_cli.config import DOMAIN_SUFFIX

columns, lines = shutil.get_terminal_size()

ERROR_LEFT_TOP = "┏━━━━ Error "
ERROR_LEFT_FIR = "┃ x "
ERROR_LEFT_MID = "┃ "
ERROR_LEFT_BOT = "┗"

ERROR_TOP = (
    click.style(ERROR_LEFT_TOP, fg="red") +
    click.style("━" * (columns - len(ERROR_LEFT_TOP)), fg="red") +
    "\n"
)
ERROR_FIR = click.style(ERROR_LEFT_FIR, fg="red")
ERROR_MID = click.style(ERROR_LEFT_MID, fg="red")
ERROR_BOT = (
    click.style(ERROR_LEFT_BOT, fg="red") +
    click.style("━" * (columns - len(ERROR_LEFT_BOT)), fg="red")
)

MSG_NO_STORE = (
    ERROR_TOP +
    ERROR_FIR +
    click.style("No store found. Please run", fg="red") +
    " " +
    click.style("funpinpin login --store STORE", fg="bright_cyan") +
    click.style(" to login to a specific store", fg="red") +
    "\n" +
    ERROR_BOT
)

MSG_NOT_LOGIN = (
    "It doesn't appear that you're logged in. " +
    "You must log into a partner organization or a store staff account.\n" +
    "If trying to log into a store staff account, please use " +
    click.style("funpinpin login --store STORE", fg="bright_cyan") +
    " to log in."
)


def get_login_msg(shop, partner_name):
    """Get login shop successfully message."""
    if not shop:
        msg = (
            "Logged into partner organization " +
            click.style(f"{partner_name}", fg="green")
        )
    else:
        msg = (
            "Logged into store " +
            click.style(f"{shop} ", fg="green") +
            "in partner organization " +
            click.style(f"{partner_name}", fg="green")
        )
    return msg


def wrap_line(
    msg: str, j: int, style_map: dict = {}
) -> Tuple[str, int]:
    """Wrap line with click style."""

    def get_style(snippet):
        for k in style_map.keys():
            if snippet in k:
                return style_map[k]
        else:
            return {"fg": "red"}
    i = j
    n_ident = msg[j: columns - 4].find("\n")
    if n_ident < 0:
        j += (columns - 4)
    else:
        j += (n_ident + 1)
    msg_snippet = click.style(
        msg[i:j],
        **get_style(msg[i:j])
    )
    msg_formatted = ERROR_FIR + msg_snippet
    if n_ident < 0:
        msg_formatted += "\n"
    return msg_formatted, j


def wrap_msg_with_style(msg, style_map):
    """Wrap display message."""
    msg_formatted = ERROR_TOP
    j = 0
    while(j <= len(msg)):
        _msg, j = wrap_line(msg, j, style_map)
        msg_formatted += _msg
    msg_formatted += ERROR_BOT
    return msg_formatted


def wrap_msg(msg):
    """Wrap display message."""
    msg_formatted = ERROR_TOP
    # ToDo:
    # if there is special style, such as underline or color,
    # tranverse msg, assign new style.
    # Temporarily, assign red.
    if (len(msg) + len(ERROR_LEFT_FIR) - columns) <= 0:
        msg_formatted += (
            ERROR_FIR +
            click.style(msg, fg="red") + "\n" +
            ERROR_BOT
        )
    else:
        msg_formatted += (
            ERROR_FIR + click.style(msg[:columns - 4], fg="red") + "\n"
        )
        msg_left = len(msg) - columns + len(ERROR_LEFT_FIR)
        msg_lines = msg_left // (columns - 2)
        j = columns - 4
        for i in range(msg_lines):
            msg_mid = ERROR_MID + click.style(
                msg[j: j + columns - 2] + "\n", fg="red"
            )
            msg_formatted += msg_mid
            j += (columns - 2)
        if j <= len(msg):
            msg_last = ERROR_MID + click.style(
                msg[j:] + "\n", fg="red"
            )
            msg_formatted += msg_last
        msg_formatted += ERROR_BOT
    return msg_formatted


def get_invalid_shop_msg(shop):
    """Get invalid shop message."""
    msg = (
        f"Invalid store provided ({shop}). " +
        "Please provide the store in the following format: " +
        f"my-store.v3.myfunpinpin.{DOMAIN_SUFFIX}"
    )
    return wrap_msg(msg)


def get_populate_begin_msg(shop):
    """Get message before populate."""
    msg = \
        "Proceeding using " + click.style(f"{shop}", fg="green")
    return msg


def get_populate_msg(shop, obj_type, obj_name, obj_id):
    """Get obj message when created successfully."""
    msg = \
        f"{obj_name} added to " + \
        click.style(f"{shop}", fg="green") + \
        " at " + \
        click.style(
            f"https://{shop}/admin/{obj_type}/{obj_id}",
            underline=True
        )
    return msg


def get_populate_end_msg(shop, obj_type, count):
    """Get message after populate."""
    msg = (
        f"Successfully added {count} {obj_type.capitalize()} to " +
        click.style(f"{shop}\n", fg="green") +
        "View all Products at " +
        click.style(f"https://{shop}/admin/{obj_type}", underline=True)
    )
    return msg


def get_switch_same_strore_msg(shop):
    """Get message when switch to the same store."""
    msg = \
        "Using development store " + \
        click.style(f"{shop}\n", fg="green") + \
        "Switched development store to " + \
        click.style(f"{shop}", fg="green")
    return msg


def get_ngrok_auth_error_msg():
    """Get ngrok auth error message."""
    msg = (
        "A free ngrok account is required: " +
        "https://ngrok.com/signup. After you signup, " +
        "install your personal authorization token using " +
        "funpinpin app tunnel auth <token>."
    )
    return wrap_msg(msg)


def get_ngrok_run_msg(account, url):
    """Get ngrok run message."""
    msg = (
        "ngrok tunnel running at " +
        click.style(f"{url}", underline=True) +
        f", with account {account}"
    )
    return msg


NGROK_CANNOT_STOPPED_MSG = (
    click.style(
        "ngrok tunnel could not be stopped. Try running ", fg="red"
    ) +
    click.style("killall -9 ngrok", fg="bright_cyan")
)


def get_ngrok_108_msg():
    """Get ngrok 108 error message."""
    msg = (
        "Another ngrok tunnel is currently running with your auth token," +
        " possibly on another machine. " +
        "Terminate that tunnel before opening a new one."
    )
    return wrap_msg(msg)


def get_ngrok_107_msg():
    """Get ngrok 107 error message."""
    msg = (
        "The ngrok token currently configured is invalid. " +
        "After generating a new token, " +
        "update your local ngrok configuration " +
        "using shopify app tunnel auth <token>"
    )
    return wrap_msg(msg)


PROJECT_TYPE_ERROR = "This command can only be run within "


APP_AUTHENTICATED_ERROR_MSG = (
    "Please ensure you've logged in with " +
    click.style("funpinpin login", fg="bright_cyan") +
    " and try again"
)


def get_app_create_msg(shop, name, api_client):
    """Get app successfully created message."""
    project_style = click.style(f"{name}", fg="green")
    install_url_style = click.style(
        f"https://partners.funpinpin.{DOMAIN_SUFFIX}/partners/apps/appTesting/{api_client['id']}?client_id={api_client['client_id']}",
        underline=True
    )
    dashboard_url_style = click.style(
        f"https://partners.funpinpin.{DOMAIN_SUFFIX}/partners/apps/info/{api_client['id']}",
        underline=True
    )

    msg = (
        project_style +
        " was created in the organization's Partner Dashboard " +
        dashboard_url_style +
        "\n" +
        "Change directories to your new project folder " +
        project_style +
        " and run " +
        click.style("funpinpin app serve", fg="bright_cyan") +
        " to start a local server" +
        "\n" +
        "Then, visit " +
        install_url_style +
        " to install " +
        click.style(f"{name}", fg="green") +
        " on your Dev Store"
    )
    return msg


NODE_INSTALL_MSG = (
    "Node.js is required to continue. Install Node.js here: " +
    click.style("https://nodejs.org/en/download", underline=True) +
    "."
)


NPM_INSTALL_MSG = (
    "npm is required to continue. Install npm here: " +
    click.style("https://www.npmjs.com/get-npm", underline=True) +
    "."
)


def get_app_serve_msg(host, shop):
    """Get app successfully serve message."""
    msg = (
        "To install and start using your app, open this URL in your browser:\n" +
        click.style(
            f"{host}/login?shop={shop}",
            fg="green"
        )
    )
    return msg


NOT_VERIFIED_SHOP_MSG = (
    "Couldn't verify your store. If you don't have a development store set up, " +
    "please create one in your Partners dashboard and run " +
    click.style("funpinpin app connect", fg="bright_cyan") +
    "."
)


NOT_IN_PROJ_MSG = (
    "You are not in a Funpinpin app project\n" +
    "Run " +
    click.style("funpinpin app create ", fg="bright_cyan") +
    "to create your app"
)


CONNECT_PROD_WARNING = (
    click.style("! Warning: if you have connected to an ", fg="yellow") +
    click.style("app in production", fg="yellow", bold=True) +
    click.style(" running ", fg="yellow") +
    click.style("serve", fg="bright_cyan") +
    click.style(" may update the app URL and cause an outage.", fg="yellow")
)


ALREADY_CONNECTED_WARNING = (
    click.style("! This app appears to be already connected", fg="yellow")
)


def get_missing_yml_msg(directory, config_name):
    """Get missing yml message."""
    msg = (
        f"Couldn't find a {config_name} file in the directory " +
        f"{directory}" +
        " to determine the app type."
    )
    return wrap_msg(msg)


def get_type_not_found_msg(directory):
    """Get project type not found message."""
    msg = (
        "Couldn't detect the app type in directory " +
        f"{directory}. " +
        "We currently support NodeJS apps."
    )
    return wrap_msg(msg)


def get_invalid_type_msg(project_type):
    """Get invalid project type message."""
    msg = (
        f"The project type {project_type} doesn't represent an app."
    )
    return wrap_msg(msg)


def get_connected_msg(app_name):
    """Get app connected message."""
    msg = (
        "Project now connected to " +
        click.style(f"{app_name}", fg="green")
    )
    return msg


def get_open_msg(shop, host):
    """Get app open message."""
    msg = (
        "Please open this URL in your browser:\n" +
        click.style(f"{host}/login?shop={shop}", fg="green")
    )
    return msg
