/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";
import { jsonrpc } from "@web/core/network/rpc_service";
import { patch } from "@web/core/utils/patch";

var debrand_title = "";

jsonrpc(
  "/web/dataset/call_kw/sh.debranding.config/search_read",
  {
    model: "sh.debranding.config",
    method: "search_read",
    args: [[], ["name"]],
    kwargs: {},
    limit: 1,
  },
  { async: false }
).then(function (output) {
  if (output && output[0]) {
    debrand_title = output[0]["name"];
  }
});

patch(Dialog.prototype, {
  setup() {
    this.props.title = debrand_title;
    super.setup();
  },
});
