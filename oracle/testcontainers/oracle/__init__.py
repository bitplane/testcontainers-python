from testcontainers.core.generic import DbContainer


class OracleDbContainer(DbContainer):
    """
    Oracle database container.

    Example:

        .. code-block::

            >>> import sqlalchemy
            >>> from testcontainers.oracle import OracleDbContainer

            >>> with OracleDbContainer() as oracle:
            ...     e = sqlalchemy.create_engine(oracle.get_connection_url())
            ...     result = e.execute("select * from V$VERSION")
    """

    def __init__(self, image: str = "wnameless/oracle-xe-11g-r2:latest", **kwargs) -> None:
        super(OracleDbContainer, self).__init__(image=image, **kwargs)
        self.container_port = 1521
        self.with_exposed_ports(self.container_port)
        self.with_env("ORACLE_ALLOW_REMOTE", "true")

    def get_connection_url(self) -> str:
        return super()._create_connection_url(
            dialect="oracle", username="system", password="oracle", port=self.container_port,
            db_name="xe"
        )

    def _configure(self) -> None:
        pass
