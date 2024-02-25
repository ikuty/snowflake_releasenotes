feed = """
<?xml version='1.0' encoding='UTF-8'?>
<feed xml:lang='ja' xmlns='http://www.w3.org/2005/Atom'>
  <title>Snowflake release notes</title>
  <description>Snowflake release notes</description>
  <updated>{updated_at}</updated>
  <link>https://docs.snowflake.com/en/release-notes/new-features</link>
{entries}
</feed>
"""[1:-1]

entry = """
<entry>
  <id>{id}</id>
  <published>{published_at}</published>
  <updated>{updated_at}</updated>
  <link rel='alternate' type='text/html' href='{url}' />
  <url>{url}</url>
  <title>{title}</title>
  <summary>{summary}</summary>
</entry>
"""[1:-1]

