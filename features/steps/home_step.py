from behave import given, then, when
from faker import Faker

fake = Faker('pt_BR')

@given(u'que acessei o site gamesclub')
def step_impl(context):
        context.scenario.home_page.link()

@when(u'eu clico no botão criar conta')
def step_impl(context):
         context.scenario.home_page.click_createaccount()

@when(u'eu clico no botão login')
def step_impl(context):
         context.scenario.home_page.click_login()

@when(u'preencho o campo login com "{login}"')
def step_impl(context, login):
        context.scenario.home_page.fill_login(login)

@then(u'devo logar na plataforma com sucesso')
def step_impl(context):
    context.scenario.home_page.check_login()

@when(u'clico no botão entrar')
def step_impl(context):
    context.scenario.home_page.click_enter()

@then(u'devo visualizar uma mensagem de erro')
def step_impl(context):
    context.scenario.home_page.view_message_erro()
