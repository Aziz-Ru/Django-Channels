# Channel

Channels wraps Django’s native asynchronous view support, allowing Django projects to handle not only HTTP, but protocols that require long-running connections too - WebSockets, MQTT, chatbots, amateur radio, and more.

It allowing you to choose how you write your code - synchronous in a style like Django views, fully asynchronous, or a mixture of both.

Channels also bundles this event-driven architecture with channel layers, a system that allows you to easily communicate between processes, and separate your project into different processes.

# Scopes and Events

Channels and ASGI split up incoming connections into two components: a scope, and a series of events.

The scope is a set of details about a single incoming connection - such as the path a web request was made from, or the originating IP address of a WebSocket, or the user messaging a chatbot.

During the lifetime of this scope, a series of events occur.These represent user interactions - making a HTTP request, for example, or sending a WebSocket frame. Your Channels or ASGI applications will be instantiated once per scope, and then be fed the stream of events happening within that scope to decide what action to take.

An example with a chatbot:

```
1.The user sends a first message to the chatbot.
2.This opens a scope containing the user’s username, chosen name, and user ID.
3.The application is given a chat.received_message event with the event text. It does not have to respond, but could send one, two or more other chat messages back as chat.send_message events if it wanted to.

4The user sends more messages to the chatbot and more chat.received_message events are generated.
After a timeout or when the application process is restarted the scope is closed.
```

# Consumers

A consumer is the basic unit of Channels code
