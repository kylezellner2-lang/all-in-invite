#!/usr/bin/env python3
"""Personal invite links. index.html is the master (generic invite).
Run `python3 build.py` after EVERY edit to index.html, then commit + push.
Each person gets <slug>/index.html -> https://kylezellner2-lang.github.io/all-in-invite/<slug>/"""
import os
PEOPLE = {"freddy": "Freddy", "noah": "Noah", "shelby": "Shelby", "salah": "Salah", "callie": "Callie"}
# People whose link shows a Deliverables block (their own compensation). Others keep the fine-print line.
COMP = {"freddy": "$7,000", "shelby": "$7,000", "salah": "$7,000"}
# Instagram account 1win adds as the collaborator (shown and linked in that person's deliverable).
ACCOUNT = {"shelby": "shelbyrobinss"}
FINE = '<p class="fine r d4">1win posts the final video on its page and adds you as a collaborator. The only requirement is that you accept the collab.</p>'
DELIV = '''<h3 class="dl r d4">Deliverables</h3>
    <div class="gets two">
      <div class="r d4"><b>1 Collab</b><span>1win posts the final video and adds %s as a collaborator. You just accept the collab.</span></div>
      <div class="r d4"><b>%s</b><span>compensation.</span></div>
    </div>'''
src = open("index.html").read()
def rep(s, a, b):
    assert s.count(a) == 1, a
    return s.replace(a, b)
for slug, name in PEOPLE.items():
    s = src
    s = rep(s, "<em>You're invited</em>", "<em>%s, you're invited</em>" % name)
    s = rep(s, '<div class="tag">You\'re invited</div>', '<div class="tag">%s, you\'re invited</div>' % name)
    s = rep(s, 'content="All In · You\'re invited"', 'content="%s, you\'re invited"' % name)
    s = rep(s, 'aria-label="You\'re invited. Open the invitation."', 'aria-label="%s, you\'re invited. Open the invitation."' % name)
    s = rep(s, '<span class="e-flap"></span>', '<span class="e-flap"></span>\n    <span class="e-name">%s</span>' % name)
    if slug in COMP:
        acct = ACCOUNT.get(slug)
        where = ('<a href="https://www.instagram.com/%s/" target="_blank" rel="noopener">@%s</a>' % (acct, acct)) if acct else "you"
        s = rep(s, FINE, DELIV % (where, COMP[slug]))
    s = s.replace('"photos/', '"../photos/')
    os.makedirs(slug, exist_ok=True)
    open(os.path.join(slug, "index.html"), "w").write(s)
    print("built", slug)
