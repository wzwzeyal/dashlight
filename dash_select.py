import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)
box_style = dict(border='1px solid', margin='15px', padding='10px')
app.layout = html.Div(id='wrapper', children=[
    html.P(id='selection-container', children='This text is selectable. Select here.', style=box_style),
    html.P(id='other-container', children='Selecting this text will not work.', style=box_style),
    dcc.Input(id='selection-text', value='', style=dict(display='none')),
    dcc.Input(id='selection-start', value='', style=dict(display='none')),
    dcc.Input(id='selection-end', value='', style=dict(display='none')),
    html.Button(id='submit', children='Submit selection'),
    html.P(id='callback-result', children=''),
])


@app.callback(
    dash.dependencies.Output('callback-result', 'children'),
    [dash.dependencies.Input('submit', 'n_clicks')],
    [
        dash.dependencies.State('selection-text', 'value'),
        dash.dependencies.State('selection-start', 'value'),
        dash.dependencies.State('selection-end', 'value'),
    ],
        )
def update_output(n_clicks, text, start, end):
    if text:
        # res = html.Span("test") + "<mark>" + "marked text" + "</mark>"
        # return res
        return html.Mark(html.Span(f'Selected string: "{text}"', style=dict(color='green')))
    return html.Span('Nothing selected', style=dict(color='red'))


if __name__ == '__main__':
    app.run_server(debug=True)