using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace BaiduAPI
{
    class Program
    {
        public static string ak = "6tVLhzwQxslkwwmprWAdppdAb4aZk40I";
        static void Main(string[] args)
        {
            List<House> houseList = JsonConvert.DeserializeObject<List<House>>(File.ReadAllText(@"Data\items_minhang_cn.json"));
            foreach (House house in houseList) {
                try
                {
                    WebRequest request = WebRequest.Create(
                    "http://api.map.baidu.com/geocoder/v2/?address=" + house.community + "&output=json&ak=" + ak + "&callback=showLocation");
                    WebResponse response = request.GetResponse();
                    //Console.WriteLine(((HttpWebResponse)response).StatusCode);
                    Stream dataStream = response.GetResponseStream();
                    StreamReader reader = new StreamReader(dataStream);
                    string res = reader.ReadToEnd();
                    res = res.Replace("showLocation&&showLocation(", "").Replace(")", "");
                    BaiduResult baiduResult = JsonConvert.DeserializeObject<BaiduResult>(res);
                    house.unitPrice = house.unitPrice.Replace("单价", "");
                    house.latitude = baiduResult.result.location.lat;
                    house.longtitude = baiduResult.result.location.lng;
                    reader.Close();
                    response.Close();
                    Console.WriteLine("Finish parse in {0}", house.community);
                }
                catch (Exception e) {
                    Console.WriteLine(e.ToString());
                }
            }
            File.WriteAllText(@"Output\items_minhang_cn.json", JsonConvert.SerializeObject(houseList));
        }
    }
}
