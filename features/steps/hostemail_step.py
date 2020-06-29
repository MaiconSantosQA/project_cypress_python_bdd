from behave import given, then, when
from faker import Faker

fake = Faker('pt_BR')

@given(u'que acessei o site hostmail')
def step_impl(context):
        context.scenario.hostemail_page.link_hostemail()

@when(u'eu preencho o campo email com "{email}"')
def step_impl(context, email):
        context.scenario.hostemail_page.fill_email(email)

@when(u'clico no botão acessar email')
def step_impl(context):
        context.scenario.hostemail_page.click_email()

@then(u'devo visualizar o email de confirmação')
def step_impl(context):
        context.scenario.hostemail_page.view_email()

@then(u'devo clicar em confirmar')
def step_impl(context):
        context.scenario.hostemail_page.click_confirm()
