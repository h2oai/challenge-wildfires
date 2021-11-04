from h2o_wave import main, app, Q, ui

# TABS FOR THE APP'S NAVIGATION MENU
tabs = [
    ui.tab(name='data', label='Data', icon='DiagnosticDataBarTooltip'),
    ui.tab(name='model', label='Model', icon='BuildDefinition'),
    ui.tab(name='predict', label='Predict', icon='CRMCustomerInsightsApp')
]

# DISPLAY HEADER AND FOOTER JUST ONCE PER CLIENT
async def init_ui(q: Q):
    q.page['header'] = ui.header_card(box='header', title='Challenge Wildfires', subtitle='H2O Olympics',
        icon='LightningBolt', icon_color='Black'
    )

    # FOOTER CARD TO DISPLAY A CAPTION OF EMBEDED HTML FOR THE FOOTER
    q.page['footer'] = ui.footer_card(
        box='footer',
            caption='Made with 💛️ using Wave. (c) 2021 H2O.ai. All rights reserved.'
    )


# DISPLAY A NAVIGATION MENU WITH TABS
async def render_menu(q:Q):
    if q.client.initialized:
        q.page['tabs'] = ui.tab_card(name='tabs', box='tabs', link=True, value=q.client.tabs, items=[
            *tabs,
        ])
        await q.page.save()


# UI_UTIL FUNCTION TO MAKE A UI.MARKDOWN_TABLE FROM A PD.DATAFRAME
async def make_markdown_table(fields, rows):
    def make_markdown_row(values):
        return f"| {' | '.join([str(x) for x in values])} |"

    return '\n'.join([
        make_markdown_row(fields),
        make_markdown_row('---' * len(fields)),
        '\n'.join([make_markdown_row(row) for row in rows]),
    ])


# EACH TIME A NEW TAB IS RENDERED, CLEAN THE 'BODY' ZONE, I.E.
# DELETE THE PAGES FOR THE OTHER TABS
async def reset_pages(q:Q):
    pages = ['df', 'map', 'models', 'metrics', 'options']

    for page in pages:
        del q.page[page]
    
    await q.page.save()
