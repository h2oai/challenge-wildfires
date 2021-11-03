from h2o_wave import main, app, Q, ui

# tabs for the app's navigation menu
tabs = [
    ui.tab(name='data', label='Data', icon='DiagnosticDataBarTooltip'),
    ui.tab(name='model', label='Model', icon='BuildDefinition'),
    ui.tab(name='predict', label='Predict', icon='CRMCustomerInsightsApp')
]

# display header and footer just once per client
async def init_ui(q: Q):
    q.page['header'] = ui.header_card(box='header', title='Challenge Wildfires', subtitle='H2O Olympics',
        icon='LightningBolt', icon_color='Black'
    )

    # footer card to display a caption of embeded HTML for the footer
    q.page['footer'] = ui.footer_card(
        box='footer',
            caption="""
<style type='text/css'>
img:hover { transform: scale(1.1); }
footer{ text-align:center; }
</style>

<footer>
<a href="https://wave.h2o.ai" target="_blank">
<img style="vertical-align:middle;" src="https://github.com/h2oai/wave/raw/master/assets/brand/wave-type-yellow.png" width="100px" height="50px">
</a>
<p>Built with H2O Wave.<br>
(c) 2021 H2O.ai. All rights reserved.</p>
</footer>
"""
    )


# display a navigation menu with tabs
async def render_menu(q:Q):
    if q.client.initialized:
        q.page['tabs'] = ui.tab_card(name='tabs', box='tabs', link=True, value=q.client.tabs, items=[
            *tabs,
        ])
        await q.page.save()


# each time a new tab is rendered, clean the 'body' zone, i.e.
# delete the pages for the other tabs
async def reset_pages(q:Q):
    pages = []

    for page in pages:
        del q.page[page]
    
    await q.page.save()
