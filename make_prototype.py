from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
from pathlib import Path
P=Path(__file__).parent
out=P/'dist/prototype.pdf'
c=canvas.Canvas(str(out),pagesize=(842,595));c.setTitle('Flat Agree - Lo-fi prototype and design notes');c.setAuthor('Jirapat Chayapong')
def text(x,y,s,size=11,font='Helvetica',width=730):
 c.setFont(font,size)
 for line in simpleSplit(s,font,size,width):c.drawString(x,y,line);y-=size*1.5
 return y

def header(n,title,sub):
 c.setFillColor(HexColor('#242d28'));text(35,557,'FLAT AGREE / WEEK 4',10,'Helvetica-Bold');text(35,519,title,27,'Helvetica-Bold');text(35,491,sub,11)
 c.setStrokeColor(HexColor('#cccccc'));c.line(35,474,807,474)
 text(35,22,'Jirapat Chayapong | GUI Design & Web Optimization',9);text(750,22,f'{n} / 3',9)

def box(x,y,w,h,label=None):
 c.setFillColor(HexColor('#f5f5f5'));c.setStrokeColor(HexColor('#8c8c8c'));c.rect(x,y,w,h,fill=1)
 c.setFillColor(HexColor('#242d28'))
 if label:text(x+10,y+h-21,label,11,'Helvetica-Bold',w-20)
def button(x,y,w,s):
 c.setStrokeColor(HexColor('#555555'));c.rect(x,y,w,27);text(x+8,y+9,s,9)
def screen(x,title):
 box(x,116,354,324,title)
 c.line(x,401,x+354,401)
header(1,'From unwritten rules to shared agreements.','Lo-fi screen flow: browse the household, then start a specific proposal.')
screen(35,'01 / HOUSE AGREEMENTS')
text(50,380,'[All rules]   [Agreed]   [Discussing]',10);box(50,298,324,65,'Quiet evenings');text(60,315,'Noise / Agreed / 3 of 3 roommates',10)
box(50,220,324,65,'Overnight guests');text(60,237,'Guests / Discussing / 1 of 3 roommates',10)
button(50,169,150,'+ Propose a rule');text(50,140,'Open a card to read and respond.',9)
screen(453,'02 / PROPOSE A RULE')
text(468,380,'Title',10);box(468,340,324,28);text(479,350,'Give a heads-up for overnight guests',10)
text(468,319,'Category [ Guests v ]',10);box(468,221,324,77,'What are we agreeing to?');text(479,255,'Explain a specific, realistic expectation.',10,width=300)
button(468,169,150,'Share proposal');text(468,140,'Starts with the proposer\'s agreement.',9)
text(35,78,'FLOW: House agreements > Propose a rule > Share > Discussing (1/3)',12,'Helvetica-Bold')
c.showPage()
header(2,'A rule needs a conversation.','Lo-fi screen flow: review the same version, respond, and help new roommates settle in.')
screen(35,'03 / RULE DETAIL & DISCUSSION')
text(50,378,'Overnight guests',17,'Helvetica-Bold');text(50,355,'Let the flat know a day before a guest stays.',10,width=322)
text(50,321,'Jirapat: waiting    Mia: agrees    Alex: waiting',10)
button(50,271,125,'I agree');button(187,271,172,'Suggest a change')
box(50,190,324,62,'Discussion');text(60,209,'Ask a question or explain your needs.',10)
text(50,158,'An edit clears old votes. Everyone responds again.',9,width=322)
screen(453,'04 / MOVING IN')
text(468,376,'Welcome to the flat',17,'Helvetica-Bold');
for y,s in [(335,'[ ] Read the agreed rules'),(299,'[ ] Introduce your routine'),(263,'[ ] Ask about anything unclear'),(227,'[ ] Make your first proposal')]:text(468,y,s,11)
button(468,167,210,'Explore house agreements');text(468,140,'Checklist progress stays in this browser.',9)
text(35,80,'AGREEMENT LOGIC: 1/3 or 2/3 = Discussing. 3/3 = Agreed.',12,'Helvetica-Bold');text(35,58,'Changing the text starts a new decision; earlier acceptance does not transfer.',11)
c.showPage()
header(3,'Design decisions & a real test plan.','Project status and reasoning - based on the Week 3 brief, not completed interview research.')
y=445
sections=[('Starting point','A new roommate needs to learn unwritten household rules, but existing roommates do not fully agree on them either. The design should make expectations visible and let everyone respond.'),('Assumptions to test','Different expectations about cleaning, noise and guests may cause friction. People may avoid speaking up. These are hypotheses. The Week 3 interview examples are fictional; no participant findings are claimed.'),('Why these screens?','Browsing rules helps newcomers find expectations. Proposals make vague expectations specific. Comments let people explain disagreements. Unanimous agreement keeps one person from imposing a rule. Revisions clear votes so approval applies to the exact current text.'),('Implementation scope','This is the first implemented build for this project, created now from the Week 3 brief. No earlier v1 or completed Week 4 research was supplied. Demo roles simulate three roommates on one device. Local browser storage persists changes; there is no shared backend, login or cross-device synchronization.'),('Short user test - not conducted yet','Ask a tester to find the kitchen agreement, propose a guest rule, and request a revision. Observe completion, hesitation and whether they understand Discussing versus Agreed. Record actual comments in Test & feedback, then export the notes. Use these results to choose the next changes.')]
for title,body in sections:
 y=text(35,y,title,12,'Helvetica-Bold');y=text(35,y-1,body,10,width=765)-16
c.save()
print(out)
