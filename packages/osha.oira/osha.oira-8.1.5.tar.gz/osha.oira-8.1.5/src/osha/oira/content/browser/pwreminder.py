# coding=utf-8
from Acquisition import aq_inner
from euphorie.content import MessageFactory as _
from plonetheme.nuplone import MessageFactory as __
from plonetheme.nuplone.browser import pwreminder
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.PasswordResetTool import InvalidRequestError
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form.button import buttonAndHandler
from zope.i18n import translate


class RequestPasswordForm(pwreminder.RequestPasswordForm):
    """Override so that we can change some labels"""

    def updateFields(self):
        super(RequestPasswordForm, self).updateFields()
        self.fields["login"].field.title = __("label_email", default="E-mail address")


class PasswordReset(pwreminder.PasswordReset):

    orig_description = pwreminder.PasswordReset.description
    extra_description = _(
        "password_policy_conditions",
        default="Your password must contain at least 5 characters, "
        "including at least one capital letter, one number and "
        "one special character (e.g. $, # or @).",
    )

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.language = getToolByName(
            context, "portal_languages"
        ).getPreferredLanguage()

    @property
    def description(self):
        description = " ".join(
            [
                translate(self.orig_description, target_language=self.language),
                translate(self.extra_description, target_language=self.language),
            ]
        )
        return description

    def updateFields(self):
        super(PasswordReset, self).updateFields()
        self.fields["login"].field.title = __("label_email", default="E-mail address")

    @buttonAndHandler(_("button_change", default="Change"), name="change")
    def handleChange(self, action):
        """Override the default behavior to call the requestPassword method
        passing the username and not the id
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        flash = IStatusMessage(self.request).addStatusMessage
        pas = getToolByName(self.context, "acl_users")
        ppr = getToolByName(self.context, "portal_password_reset")
        user = pas.getUser(data["login"])
        if user is None:
            flash(
                __(
                    "user_name_wrong",
                    "The login name you have provided does not match the username from the password-reset email. Please check your spelling.",  # noqa: E501
                ),
                "error",
            )
            return
        # osha Patch: we need to translate the reset request
        # because we use the username and not the id
        record = ppr._requests.get(self.randomstring, ())
        if record and record[0] == user.getUserId():
            ppr._requests[self.randomstring] = (
                user.getUserName(),
                record[1],
            )
        try:
            ppr.resetPassword(
                # The osha patch is taking the username instead of the id
                # original code was:
                # user.getId(), self.randomstring, data["password"]
                user.getUserName(),
                self.randomstring,
                data["password"],
            )
        except InvalidRequestError:
            flash(
                __(
                    "user_name_wrong",
                    "The login name you have provided does not match the username from the password-reset email. Please check your spelling.",  # noqa: E501
                ),
                "error",
            )
            return

        flash(_("password_reset", "Your password has been reset."), "success")
        portal_url = aq_inner(self.context).absolute_url()
        self.request.response.redirect("%s/@@login" % portal_url)
