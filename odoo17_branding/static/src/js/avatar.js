/* @odoo-module */

import { ThreadService, threadService } from "@mail/core/common/thread_service";
import { useState } from "@odoo/owl";

import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";
import { useService } from "@web/core/utils/hooks";

patch(ThreadService.prototype, {

    avatarUrl(author, thread) {
        if (thread?.type === "livechat" && author?.type === "guest") {
            return '/web/binary/company_logo?company_id=' + session.company_id;
        }
        return super.avatarUrl(author, thread);
    },

});
