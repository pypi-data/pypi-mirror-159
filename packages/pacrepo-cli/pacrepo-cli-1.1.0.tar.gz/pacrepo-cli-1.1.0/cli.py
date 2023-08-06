import click
import configparser

class Config:
    def __init__(self,file='/etc/pacman.conf',dryrun=False):
        self.file=file
        self.dryrun=dryrun
        self.write=False

    def __enter__(self):
        self.config=configparser.ConfigParser(allow_no_value=True,default_section='options',strict=False)
        self.config.optionxform=str
        self.config.read(self.file)
        return self

    def sections(self):
        return self.config.sections()

    def has_section(self,name):
        return self.config.has_section(name)

    def remove_section(self,name):
        if self.config.has_section(name) is False:
            return
        self.write=True
        self.config.remove_section(name)

    def add_section(self,name):
        if self.config.has_section(name):
            return
        self.write=True
        self.config.add_section(name)

    def set(self,section,key,value):
        self.write=True
        self.config.set(section,key,value)

    def __exit__(self,exc_type,exc_value,tb):
        if self.dryrun:
            click.echo("Dry Run Enabled: Skipping Writing Config")
            if self.write:
                click.echo("Dry Run has blocked an update")
        if self.write is True and self.dryrun is False:
            with open(self.file,"w",encoding="utf-8") as fh:
                self.config.write(fh)

@click.group()
@click.pass_context
@click.option('--file',default='/etc/pacman.conf',help='Path to pacman.conf')
@click.option('--dryrun',is_flag=True,help='Do not write changes')
def cli(ctx,file,dryrun):
    ctx.obj=ctx.with_resource(Config(file,dryrun))

@cli.command('add')
@click.pass_obj
@click.option('--siglevel',default='',help='Set custom SigLevel For Repo')
@click.argument('name')
@click.argument('server')
def add(obj,siglevel,name,server):
    if obj.has_section(name):
        click.echo("Section already exists: {}".format(name))
        return
    obj.add_section(name)
    if siglevel!='':
        obj.set(name,'SigLevel',siglevel)
    if server.startswith("/"):
        obj.set(name,"Include",server)
    else:
        obj.set(name,"Server",server)

@cli.command('list')
@click.pass_obj
def list(obj):
    click.echo('Sections:')
    click.echo(", ".join(obj.sections()))

@cli.command('remove')
@click.pass_obj
@click.argument('name')
def remove(obj,name):
    obj.remove_section(name)

def main():
    return cli(obj={})

if __name__ == '__main__':
    main()