using System;
using System.Net;
using KRPC.Client;
using KRPC.Client.Services.KRPC;

namespace KSPKRPCTEST
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var connection = new Connection(
                   name: "EXAMPLE",
                   address: IPAddress.Parse("127.0.0.1"),
                   rpcPort: 50000,
                   streamPort: 50001))
            {
                var krpc = connection.KRPC();
            }
        }
    }
}
