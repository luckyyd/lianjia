using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BaiduAPI
{
    public class BaiduResult
    {
        public int status { get; set; }
        public Result result { get; set; }
        public int precise { get; set; }
        public int confidence { get; set; }
        public string level { get; set; }
    }

    public class Result
    {
        public Location location { get; set; }
    }

    public class Location
    {
        public string lng { get; set; }
        public string lat { get; set; }
    }
}
