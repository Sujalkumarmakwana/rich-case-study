from rich.console import Console

text = 'Error in job [link=https://www.example.com/issues/42]78351748-9b32-4e08-ad3e-7e9ff124d541: see /var/log/myapp.log[/link] for details'
url = "https://www.example.com/issues/42"

for h in (False, True):
    console = Console(force_terminal=True)
    with console.capture() as cap:
        console.print(text, highlight=h)
    print("highlight =", h, "-> link URL appears", cap.get().count(url), "time(s)")
