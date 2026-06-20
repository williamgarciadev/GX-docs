---
title: "User Control - GxChart Runtime Render File"
source_id: 4948
source_url: https://wiki.genexus.com/commwiki/wiki?4948
genexus_version: "18"
---

# User Control - GxChart Runtime Render File

```
function gxChart()
{
    this.Type="Bar";
   
    this.Title="";
    this.X_AxisTitle="";
    this.Y_AxisTitle="";
   
    this.Width = "400";
    this.Height = "400";
   
    this.DrawShadows = 1;
    this.DrawBorder = 1;
    this.ShowValues = 1;
    this.LegendPosition = "Left";
   
    this.BackgroundColor1;
    this.BackgroundColor2;
    this.GraphColor1;
    this.GraphColor2;
    this.Opacity = 255;
    this.Scale="auto";
   
    this.Categories = "Categories=Values:Category 1,Category 2, Category 3";
    this.Series = "&Series1=Values:Serie 1:96,35,23&Series2=Values:Serie 2:50,60,75";
   
    this.ServiceUrl="http://www.gxchart.com/service/";
    this.m_data;
   
    this.SetData = function(data)
    {
        this.Categories = "&Categories=Values:";
        this.Series = "";
       
        this.m_data = data;
        for(i=0;data.Categories[i]!=undefined;i++)
            this.Categories+=data.Categories[i]+",";

        this.Categories = this.Categories.substring(0,this.Categories.length-1);
       
        for(i=0;data.Series[i];i++)
        {
             this.Series+="&Series"+(i+1)+"=Values:"+data.Series[i].Name+":";
             for(x=0;data.Series[i].Values[x]!=undefined;x++)
                this.Series+=strReplace(data.Series[i].Values[x],",",".")+",";
               
             this.Series = this.Series.substring(0,this.Series.length-1);
        }
       
    }
   
    this.GetData = function()
    {
        return this.m_data;
    }
   
    this.show = function()
    {
  
        var buff = "";
        buff+="<img src=\""+this.ServiceUrl+"Drawchart.aspx?type=" + this.Type;
        buff+="&Title="+this.Title;
        buff+="&Width="+this.Width;
        buff+="&Height="+this.Height;
        buff+="&domtitle="+ this.X_AxisTitle;
        buff+="&rantitle=" + this.Y_AxisTitle;
        buff+="&shadow=" + this.DrawShadows;
        buff+="&border=" + this.DrawBorder;
        buff+="&values=" + this.ShowValues;
        buff+="&legend=" + this.LegendPosition;
        buff+="&alpha=" + this.Opacity;
        buff+="&bgc1="+this.BackgroundColor1.R+","+this.BackgroundColor1.G+","+this.BackgroundColor1.B;
        buff+="&bgc2="+this.BackgroundColor2.R+","+this.BackgroundColor2.G+","+this.BackgroundColor2.B;
        buff+="&gbgc1="+this.GraphColor1.R+","+this.GraphColor1.G+","+this.GraphColor1.B;
        buff+="&gbgc2="+this.GraphColor2.R+","+this.GraphColor2.G+","+this.GraphColor2.B;
        buff+=this.Categories;
        buff+=this.Series;
        buff+="&scale="+this.Scale;
       
        buff+="\" />";
        
        document.getElementById(this.ContainerName).innerHTML = buff.toString();
    }
   
    function strReplace(s, r, w)
    {
        return s.split(r).join(w);
    }
}
```
