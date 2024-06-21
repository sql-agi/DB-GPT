export const DATABASE_OBJECT = {
  mysql: { label: 'MySQL', icon: '/icons/mysql.png', desc: '快速、可靠、可扩展的开源关系数据库管理系统。' },
  mssql: { label: 'MSSQL', icon: '/icons/mssql.png', desc: '强大、可扩展、安全的Microsoft关系数据库系统。' },
  duckdb: { label: 'DuckDB', icon: '/icons/duckdb.png', desc: '具有高效查询处理功能的内存分析数据库。' },
  sqlite: { label: 'Sqlite', icon: '/icons/sqlite.png', desc: '具有简单性和可移植性的轻量级嵌入式关系数据库。' },
  clickhouse: {
    label: 'ClickHouse',
    icon: '/icons/clickhouse.png',
    desc: '用于高性能分析和实时查询的列式数据库。',
  },
  oracle: { label: 'Oracle', icon: '/icons/oracle.png', desc: '企业中广泛使用的健壮、可扩展、安全的关系数据库。' },
  access: {
    label: 'Access',
    icon: '/icons/access.png',
    desc: '易于使用的关系数据库，适用于Microsoft的小型应用程序。',
  },
  mongodb: { label: 'MongoDB', icon: '/icons/mongodb.png', desc: '用于web和移动应用程序的灵活、可扩展的NoSQL文档数据库。' },
  doris: { label: 'ApacheDoris', icon: '/icons/doris.png', desc: '新一代开源实时数据仓库。' },
  starrocks: { label: 'StarRocks', icon: '/icons/starrocks.png', desc: '一个开源、高性能的分析数据库。' },
  db2: { label: 'DB2', icon: '/icons/db2.png', desc: 'IBM开发的可扩展、安全的关系数据库系统。' },
  hbase: {
    label: 'HBase',
    icon: '/icons/hbase.png',
    desc: '用于大型结构化/半结构化数据的分布式、可扩展的NoSQL数据库。',
  },
  redis: { label: 'Redis', icon: '/icons/redis.png', desc: '快速、通用的内存数据结构存储为缓存、数据库或代理。' },
  cassandra: {
    label: 'Cassandra',
    icon: '/icons/cassandra.png',
    desc: '可扩展、容错的分布式大型数据NoSQL数据库。',
  },
  couchbase: {
    label: 'Couchbase',
    icon: '/icons/couchbase.png',
    desc: '分布式体系结构的高性能NoSQL文档数据库。',
  },
  postgresql: {
    label: 'PostgreSQL',
    icon: '/icons/postgresql.png',
    desc: '强大的开源关系数据库，具有可扩展性和SQL标准。',
  },
  spark: { label: 'Spark', icon: '/icons/spark.png', desc: '用于大规模数据分析的统一引擎。' },
  hive: { label: 'Hive', icon: '/icons/hive.png', desc: '一种分布式容错数据仓库系统。' },
  space: { label: 'Space', icon: '/icons/knowledge.png', desc: '知识分析。' },
  tugraph: {
    label: 'TuGraph',
    icon: '/icons/tugraph.png',
    desc: '蚂蚁集团与清华大学联合开发的高性能图形数据库。',
  },
};
export const DB_LIST = Object.entries(DATABASE_OBJECT);
