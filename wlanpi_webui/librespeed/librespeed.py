from flask import current_app, render_template, request

from wlanpi_webui.librespeed import bp


@bp.route("/")
@bp.route("/librespeed")
def librespeed():
    spt_port = "8080"
    base = request.host.split(":")[0]
    iframe = f"http://{base}:{spt_port}/speedtest.html"
    return render_template(
        "/public/librespeed.html",
        wlanpi_version=current_app.config["WLANPI_VERSION"],
        webui_version=current_app.config["WEBUI_VERSION"],
        hostname=current_app.config["HOSTNAME"],
        title=current_app.config["TITLE"],
        iframe=iframe,
    )


@bp.route("/librespeed/details")
def librespeed2():
    spt_port = "8080"
    base = request.host.split(":")[0]
    iframe = f"http://{base}:{spt_port}/alternate/speedtest.html"
    return render_template(
        "/public/librespeed.html",
        wlanpi_version=current_app.config["WLANPI_VERSION"],
        webui_version=current_app.config["WEBUI_VERSION"],
        hostname=current_app.config["HOSTNAME"],
        title=current_app.config["TITLE"],
        iframe=iframe,
    )
