/*! For license information please see 17.e15ef88f.chunk.js.LICENSE.txt */
(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[17],{1501:function(t,e){},1502:function(t,e){},1659:function(t,e){},1818:function(t,e,i){"use strict";i.r(e),i.d(e,"default",(function(){return d}));var n=i(0),r=i(1717),c=i(1657),a=i(24),h=i(212),o=i(10),s=Object(o.a)("div",{target:"e1p558ko0"})((function(t){return{"& *":{fontFamily:t.theme.genericFonts.bodyFont,fontSize:"9.6px"},"& svg":{maxWidth:"100%"}}}),""),u=i(1);c.graphviz;var d=Object(h.a)((function(t){var e=t.width,i=t.element,c=t.height,h="graphviz-chart-".concat(i.elementId),o=0,d=0,g=function(){var t=d,n=o;return c?(t=e,n=c):i.useContainerWidth&&(t=e),{chartWidth:t,chartHeight:n}},f=function(){try{var t=Object(r.a)("#".concat(h)).graphviz().zoom(!1).fit(!0).scale(1).renderDot(i.spec).on("end",(function(){var t=Object(r.a)("#".concat(h," > svg")).node();t&&(o=t.getBBox().height,d=t.getBBox().width)})),e=g(),n=e.chartHeight,c=e.chartWidth;n>0&&t.height(n),c>0&&t.width(c)}catch(s){Object(a.b)(s)}};Object(n.useEffect)((function(){f()}));var v=g(),b=v.chartWidth?v.chartWidth:e,p=v.chartHeight?v.chartHeight:c;return Object(u.jsx)(s,{className:"graphviz stGraphVizChart",id:h,style:{width:b,height:p}})}))}}]);