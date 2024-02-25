feed = """
<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='ja'>
  <title>Snowflake release notes</title>
  <updated>{updated_at}</updated>
{entries}
</feed>
"""[1:-1]

entry = """
<entry>
  <id>{id}</id>
  <title>{title}</title>
  <link rel='alternate' type='text/html' href='{url}' />
  <updated>{updated_at}</updated>
  <summary>{summary}</summary>
</entry>
"""[1:-1]

