# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import api, fields, models
from lxml import etree


class Users(models.Model):
    """ Update of res.users class
        - add a preference about sending emails about notifications
        - make a new user follow itself
        - add a welcome message
        - add suggestion preference
        - if adding groups to an user, check mail.channels linked to this user
    """
    _inherit = 'res.users'

    notification_type = fields.Selection([
        ('email', 'Handle by Emails'),
        ('inbox', 'Handle in Company')],
        'Notification Management', required=True, default='email',
        help="Policy on how to handle Chatter notifications:\n"
             "- Emails: notifications are sent to your email\n"
             "- Planet Odoo: notifications appear in your Planet Odoo Inbox")


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    @api.model
    def fields_view_get(self, view_id=None, view_type="form", toolbar=False, submenu=False):

        res = super(ResConfigSettings, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )

        page_name = res["name"]
        if not page_name == "res.config.settings.view.form":
            return res

        doc = etree.XML(res["arch"])
        enterprise_query = "//div[div[field[@widget='upgrade_boolean']]]"
        for item in doc.xpath(enterprise_query):
            item.set('style', 'display:none')

        res["arch"] = etree.tostring(doc)
        return res
class DebrandingConfig(models.Model):
    _name = 'sh.debranding.config'
    _description = 'Debranding Configuration'

    name = fields.Char("App Name", default="Savy")
    url = fields.Char("App URL")
    bot_user = fields.Char('Bot User')
    bot_user_login = fields.Char("Bot User Login")
    # favicon = fields.Binary(string="Company Favicon",
    #                         help="This field holds the image used to display a favicon for a given company.")
    avatar = fields.Binary(
        string="Avatar Image", help="This field holds the image used to display a Avatar.")

    show_support_url = fields.Boolean("Support URL ?")
    show_account_url = fields.Boolean("Account URL ?")
    show_doc_url = fields.Boolean("Documentation URL ?")

    support_url = fields.Char("Support URL")
    doc_url = fields.Char("Documentation URL")
    online_url = fields.Char("Account URL")

    def write(self, vals):
        res = super(DebrandingConfig, self).write(vals)
        if vals.get('avatar', False):
            bot_user = self.env['res.users'].sudo().search(
                [('id', '=', 1), ('active', '=', False)])
            bot_user.write({'image_1920': vals.get('avatar')})

        if vals.get('bot_user') or vals.get('bot_user_login'):
            # self._cr.execute("Update res_users set login='%s' where id=1;Update res_partner set email='%s',name='%s',display_name='%s' where id=2;" % (
                # self.bot_user_login, self.bot_user_login, self.bot_user, self.bot_user,))

            self._cr.execute("Update res_users set login='%s' where id=1;Update res_partner set email='%s',name='%s' where id=2;" % (
                self.bot_user_login, self.bot_user_login, self.bot_user))


        return res
