def queueRequests(target, wordlists):
	engine = RequestsEngine(endpoint=target.endpoint,
					concurrentConnections=1,
					requestsPerConnection=500,
					pipeline=False
                              )

	engine.queue(target.req, pauseMarker=['\r\n\r\n\'], pauseTime=61000)
	engine.queue(target.req)

def handleResponse(req, interesting):
	table.add(req)
