#davebot

##What is davebot?
Davebot is a simple chat bot written using Tornado's `ioloop` and `iostream`. 
The plan is for him to speak IRC.
Right now he is really basic but the framework is there. He will hopefully
do all sorts of useful things like give bus route info and know WolframAlpha
like the back of his robotic arm.

##Why?
I wanted to learn about the internals of Tornado and felt like this would be
a pretty good way of going about that.

##What does it do right now?
Right now davebot does _almost_ nothing. There is `TextAdapter`, an adapter 
for simple text processing over a network. The connections are made using Tornado
and so davebot is asynchronous. The next step is to write 
the `IRCAdapter` to parse messages formatted as sent by an IRC server.

After `IRCAdapter` is written then I'd like to break out the actual
chatbot scripts so that those can be in separate files and loaded at
runtime.

If I can accomplish those two goals, I'll consider davebot a success.

##How do I help?
Just make sure you have the required modules installed by running
`pip install -r requirements.txt` inside the root of this git repo. You should
then be able to run davebot and help me reach his full potential!
