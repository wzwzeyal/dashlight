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
    dash.dependencies.Output('selection-container', 'children'),
    dash.dependencies.Input('submit', 'n_clicks'),
    [
        dash.dependencies.State('selection-container', 'children'),
        dash.dependencies.State('selection-text', 'value'),
        dash.dependencies.State('selection-start', 'value'),
        dash.dependencies.State('selection-end', 'value'),
    ],
        )
def update_output(n_clicks, raw_text, res_text, start, end):
    if res_text:
        # res = html.Span("test") + "<mark>" + "marked text" + "</mark>"
        # return res

        startint = int(start)
        endint = int(end)
        before = raw_text[0:startint]
        highlight = raw_text[startint:endint]
        after = raw_text[endint:len(raw_text)]
        highlight_text = [before, html.Mark(highlight), after]

        return raw_text, highlight_text
        # return html.Mark(html.Span(f'Selected string: "{text}"', style=dict(color='green')))
    return html.Span('Nothing selected', style=dict(color='red')), dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)