import click
import markdown2
import re


@click.command()
@click.option('-i', help='path of the file you want to convert.')
@click.option('-o', help='path of the directory you want to create your html')
@click.option('-a', help = 'Readable by Germans type y')

def convertion (i, o, a):

    """Convert markdown into HTML"""

    remplaceur = ""
    title = input('title of your page: ')    
    
    #open and read Markdown file

    f = open(i, 'r', encoding = "utf-8")
    lignes = f.readlines()
    f.close()
    i = 0

    for ligne in lignes:

        #transform Markdown in html:
        
        liens = re.findall(r'http{1}s?.+.[a-z]{2,4}\S*', ligne) 

        if len(liens)>0:

            for lien in liens:
                
                r = '<a href="' + lien + '">' + lien + '</a>'
                html = re.sub(r'http{1}s?.+.[a-z]{2,4}\S*', r, ligne, count=1)
                
        else:

            md = lignes[i]
            md = md.lstrip()          
            html = markdown2.markdown(md) 

        remplaceur += html
        i += 1
        
    #option -a
 
    if a == 'y':
        
        remplaceur = remplaceur.replace("ss", "z").replace("s", "z")
        remplaceur = remplaceur.replace("qu", "k").replace("ph", "f")
        remplaceur = remplaceur.replace("g", "ch").replace("c", "k")
        remplaceur = remplaceur.replace("v", "f")
        
    page = open(o + "\index.html", 'w')  

    #html template
    
    page.write('''
    <!DOCTYPE html>
    <html>
        <head>
            <title>{}</title>
        </head>

        <body>
            {}
        </body>
    </html>
    '''.format(title, remplaceur))      

if __name__ == '__main__':
    
    convertion()    