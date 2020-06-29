from behave import given, then, when
from faker import Faker

fake = Faker('pt_BR')

@when(u'preencho o campo email com "{email}"')
def step_impl(context,email):
        context.scenario.createaccount_page.fill_email(email)

@when(u'preencho o campo confirmação de email com "{email}"')
def step_impl(context, email):
        context.scenario.createaccount_page.fill_cemail(email)

@when(u'preencho o campo senha com "{password}"')
def step_impl(context,password):
        context.scenario.createaccount_page.fill_password(password)

@when(u'devo clicar em cadastrar')
def step_impl(context):
        context.scenario.createaccount_page.click_register()

@when(u'preencho o campo nome com "{name}"')
def step_impl(context, name):
        context.scenario.createaccount_page.fill_name(name)

@when(u'preencho o campo apelido com "{nickname}"')
def step_impl(context, nickname):
        context.scenario.createaccount_page.fill_nickname(nickname)

@when(u'devo clicar no botão proximo')
def step_impl(context):
        context.scenario.createaccount_page.click_next()

@then(u'devo visualizar a mensagem de sucesso')
def step_impl(context):
        context.scenario.createaccount_page.view_congratulation()
