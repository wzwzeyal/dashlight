import dash
import dash_html_components as html
import dash_core_components as dcc

from dash import Dash, dcc, html, Input, Output, callback_context, no_update

init_text = '01234567890123456789'

app = dash.Dash(__name__)
box_style = dict(border='1px solid', margin='15px', padding='10px')
app.layout = html.Div(id='wrapper', children=[
    html.P(id='selection-container', children=init_text, style=box_style),
    html.P(id='highlight-container', children=init_text, style=box_style),
    dcc.Input(id='selection-text', value='', style=dict(display='none')),
    dcc.Input(id='selection-start', value='', style=dict(display='none')),
    dcc.Input(id='selection-end', value='', style=dict(display='none')),
    dcc.Input(id='raw_text2', value='', style=dict(display='none')),
    dcc.Input(id='raw_text', value='', style=dict(display='none')),
    
    html.Button(id='submit', children='Submit selection'),
    html.P(id='callback-result', children=''),
])


@app.callback(
    dash.dependencies.Output('callback-result', 'children'),
    # dash.dependencies.Output('highlight-container', 'children'),
    dash.dependencies.Output('selection-container', 'children'),
    [
        dash.dependencies.Input('submit', 'n_clicks'),
        dash.dependencies.Input('raw_text2', 'value'),
    ],
    [
        dash.dependencies.State('raw_text', 'value'),
        dash.dependencies.State('selection-text', 'value'),
        dash.dependencies.State('selection-start', 'value'),
        dash.dependencies.State('selection-end', 'value'),
    ],
        )
def update_output(n_clicks, raw_text2, raw_text, res_text, start, end):
    trigger = callback_context.triggered[0]
    print(trigger)

    if trigger['prop_id']=='raw_text2.value':
        return dash.no_update, raw_text2
    else:    
        if res_text:
            startint = int(start)
            endint = int(end)
            before = raw_text[0:startint]
            highlight = html.Mark(raw_text[startint:endint])
            # highlight = raw_text[startint:endint]
            after = raw_text[endint:len(raw_text)]
            highlight_text = [before, highlight, after]
            return res_text, highlight_text
        # return html.Mark(html.Span(f'Selected string: "{text}"', style=dict(color='green')))
    return html.Span('Nothing selected', style=dict(color='red')), dash.no_update


# @app.callback(
#     dash.dependencies.Output('highlight-container', 'children'),
#     dash.dependencies.Input('raw_text2', 'value'),
#         )
# def clear_text(raw_text2):
#     return raw_text2

if __name__ == '__main__':
    app.run_server(debug=True)