// usefull to be run on browser consoles, because it will keep cookies context
// Which is Scope 1.0 authentication method
function request(url, method='GET', body={}) {
    if (method === 'GET') {
        let response = fetch(url).then(res => res.json()).then(console.log)
    }
    else if (method === 'POST' || method === 'PUT' || method === 'DELETE' || method === 'PATCH')
    {
        let response = fetch(
            url,
            {
                method,
                body: JSON.stringify(body),
                'headers': {'Content-type': 'application/json; charset=UTF-8'}
            }
        ).then(res => res.json()).then(console.log)
    }
    else
    {
        console.log(`Invalid request method: {method}`)
    }
}
