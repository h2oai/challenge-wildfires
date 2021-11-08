from h2o_wave import main, app, Q, ui

# Tabs for the app's navigation menu.
tabs = [
    ui.tab(name='data', label='Data', icon='DiagnosticDataBarTooltip'),
    ui.tab(name='model', label='Model', icon='BuildDefinition'),
    ui.tab(name='predict', label='Predict', icon='CRMCustomerInsightsApp')
]

# Display header and footer just once per client.
async def init_ui(q: Q):
    q.page['header'] = ui.header_card(box='header', title='Challenge Wildfires', subtitle='H2O Olympics',
        icon='LightningBolt', icon_color='Black'
    )

    # Footer card to display a caption of embeded html for the footer.
    q.page['footer'] = ui.footer_card(
        box='footer',
            caption='Made with 💛️ using H2O Wave.'
    )


# Display a navigation menu with tabs.
async def render_menu(q:Q):
    if q.client.initialized:
        q.page['tabs'] = ui.tab_card(name='tabs', box='tabs', link=True, value=q.client.tabs, items=[
            *tabs,
        ])
        await q.page.save()


# UI util function to make a ui.markdown_table from a pd.dataframe.
async def make_markdown_table(fields, rows):
    def make_markdown_row(values):
        return f"| {' | '.join([str(x) for x in values])} |"

    return '\n'.join([
        make_markdown_row(fields),
        make_markdown_row('---' * len(fields)),
        '\n'.join([make_markdown_row(row) for row in rows]),
    ])


# Each time a new tab is rendered, clean the 'body' zone, i.e. delete the pages for the other tabs.
async def reset_pages(q:Q):
    pages = ['df', 'map', 'models', 'metrics', 'options']

    for page in pages:
        del q.page[page]
    
    await q.page.save()
