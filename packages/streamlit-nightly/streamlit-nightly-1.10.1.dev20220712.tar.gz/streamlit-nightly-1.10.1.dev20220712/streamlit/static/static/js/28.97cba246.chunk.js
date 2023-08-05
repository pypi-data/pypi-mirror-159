/*! For license information please see 28.97cba246.chunk.js.LICENSE.txt */
(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[28],{1817:function(e,t,a){"use strict";a.r(t),a.d(t,"default",(function(){return T}));var n=a(5),r=a(17),i=a(8),s=a.n(i),o=a(67),u=a(2),c=a(4),l=a(6),h=a(7),d=a(0),f=a(74),p=a(24),v=a(47),g=a(212),b=a(96),m=a(131),w=a(1520),y=a(1253),x=a(10),O=Object(x.a)("div",{target:"everg990"})((function(e){var t=e.theme;return{"&.vega-embed":{".vega-actions":{zIndex:t.zIndices.popupMenu},summary:{height:"auto",zIndex:t.zIndices.menuButton}}}}),""),j=a(1),V="(index)",D="source",k=new Set([m.a.DatetimeIndex,m.a.Float64Index,m.a.Int64Index,m.a.RangeIndex,m.a.UInt64Index]),z=function(e){Object(l.a)(a,e);var t=Object(h.a)(a);function a(){var e;Object(u.a)(this,a);for(var n=arguments.length,r=new Array(n),i=0;i<n;i++)r[i]=arguments[i];return(e=t.call.apply(t,[this].concat(r))).vegaView=void 0,e.vegaFinalizer=void 0,e.defaultDataName=D,e.element=null,e.state={error:void 0},e.finalizeView=function(){e.vegaFinalizer&&e.vegaFinalizer(),e.vegaFinalizer=void 0,e.vegaView=void 0},e.generateSpec=function(){var t=e.props,a=t.element,n=t.theme,r=JSON.parse(a.spec),i=a.useContainerWidth;if(r.config=S(r.config,n),e.props.height?(r.width=e.props.width-38,r.height=e.props.height):i&&(r.width=e.props.width-38),r.padding||(r.padding={}),null==r.padding.bottom&&(r.padding.bottom=20),r.datasets)throw new Error("Datasets should not be passed as part of the spec");return r},e}return Object(c.a)(a,[{key:"componentDidMount",value:function(){var e=Object(o.a)(s.a.mark((function e(){var t;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,this.createView();case 3:e.next=9;break;case 5:e.prev=5,e.t0=e.catch(0),t=Object(b.a)(e.t0),this.setState({error:t});case 9:case"end":return e.stop()}}),e,this,[[0,5]])})));return function(){return e.apply(this,arguments)}}()},{key:"componentWillUnmount",value:function(){this.finalizeView()}},{key:"componentDidUpdate",value:function(){var e=Object(o.a)(s.a.mark((function e(t){var a,n,i,o,u,c,l,h,d,f,v,g,m,w,y,x,O,j,V,D,k,z;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(a=t.element,n=t.theme,i=this.props,o=i.element,u=i.theme,c=a.spec,l=o.spec,this.vegaView&&c===l&&n===u&&t.width===this.props.width&&t.height===this.props.height){e.next=16;break}return Object(p.c)("Vega spec changed."),e.prev=6,e.next=9,this.createView();case 9:e.next=15;break;case 11:e.prev=11,e.t0=e.catch(6),h=Object(b.a)(e.t0),this.setState({error:h});case 15:return e.abrupt("return");case 16:for(d=a.data,f=o.data,(d||f)&&this.updateData(this.defaultDataName,d,f),v=I(a)||{},g=I(o)||{},m=0,w=Object.entries(g);m<w.length;m++)y=Object(r.a)(w[m],2),x=y[0],O=y[1],j=x||this.defaultDataName,V=v[j],this.updateData(j,V,O);for(D=0,k=Object.keys(v);D<k.length;D++)z=k[D],g.hasOwnProperty(z)||z===this.defaultDataName||this.updateData(z,null,null);this.vegaView.resize().runAsync();case 24:case"end":return e.stop()}}),e,this,[[6,11]])})));return function(t){return e.apply(this,arguments)}}()},{key:"updateData",value:function(e,t,a){if(!this.vegaView)throw new Error("Chart has not been drawn yet");if(a&&0!==a.data.numRows)if(t&&0!==t.data.numRows){var n=t.dimensions,r=n.dataRows,i=n.dataColumns,s=a.dimensions,o=s.dataRows;if(function(e,t,a,n,r,i){if(a!==i)return!1;if(t>=r)return!1;if(0===t)return!1;var s=i-1,o=t-1;if(e.getDataValue(0,s)!==n.getDataValue(0,s)||e.getDataValue(o,s)!==n.getDataValue(o,s))return!1;return!0}(t,r,i,a,o,s.dataColumns))r<o&&this.vegaView.insert(e,N(a,r));else{var u=y.changeset().remove(y.truthy).insert(N(a));this.vegaView.change(e,u),Object(p.c)("Had to clear the ".concat(e," dataset before inserting data through Vega view."))}}else this.vegaView.insert(e,N(a));else this.vegaView._runtime.data.hasOwnProperty(e)&&this.vegaView.remove(e,y.truthy)}},{key:"createView",value:function(){var e=Object(o.a)(s.a.mark((function e(){var t,a,n,i,o,u,c,l,h,d,f,v,g,b,m,y;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(Object(p.c)("Creating a new Vega view."),this.element){e.next=3;break}throw Error("Element missing.");case 3:return this.finalizeView(),t=this.props.element,a=this.generateSpec(),e.next=8,Object(w.a)(this.element,a);case 8:if(n=e.sent,i=n.vgSpec,o=n.view,u=n.finalize,this.vegaView=o,this.vegaFinalizer=u,c=F(t),1===(l=c?Object.keys(c):[]).length?(h=Object(r.a)(l,1),d=h[0],this.defaultDataName=d):0===l.length&&i.data&&(this.defaultDataName=D),(f=C(t))&&o.insert(this.defaultDataName,f),c)for(v=0,g=Object.entries(c);v<g.length;v++)b=Object(r.a)(g[v],2),m=b[0],y=b[1],o.insert(m,y);return e.next=22,o.runAsync();case 22:this.vegaView.resize().runAsync();case 23:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this;if(this.state.error)throw this.state.error;return Object(j.jsx)(O,{"data-testid":"stArrowVegaLiteChart",ref:function(t){e.element=t}})}}]),a}(d.PureComponent);function C(e){var t=e.data;return t&&0!==t.data.numRows?N(t):null}function F(e){var t=I(e);if(null==t)return null;for(var a={},n=0,i=Object.entries(t);n<i.length;n++){var s=Object(r.a)(i[n],2),o=s[0],u=s[1];a[o]=N(u)}return a}function I(e){var t;if(0===(null===(t=e.datasets)||void 0===t?void 0:t.length))return null;var a={};return e.datasets.forEach((function(e){if(e){var t=e.hasName?e.name:null;a[t]=e.data}})),a}function N(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0;if(e.isEmpty())return[];for(var a=[],n=e.dimensions,r=n.dataRows,i=n.dataColumns,s=m.b.getTypeName(e.types.index[0]),o=k.has(s),u=t;u<r;u++){var c={};if(o){var l=e.getIndexValue(u,0);c[V]="bigint"===typeof l?Number(l):l}for(var h=0;h<i;h++){var d=e.getDataValue(u,h);c[e.columns[0][h]]="bigint"===typeof d?Number(d):d}a.push(c)}return a}function S(e,t){var a=t.colors,r=t.fontSizes,i=t.genericFonts,s={labelFont:i.bodyFont,titleFont:i.bodyFont,labelFontSize:r.twoSmPx,titleFontSize:r.twoSmPx},o={background:a.bgColor,axis:Object(n.a)({labelColor:a.bodyText,titleColor:a.bodyText,gridColor:a.fadedText10},s),legend:Object(n.a)({labelColor:a.bodyText,titleColor:a.bodyText},s),title:Object(n.a)({color:a.bodyText,subtitleColor:a.bodyText},s),header:{labelColor:a.bodyText}};return e?Object(v.merge)({},o,e||{}):o}var T=Object(f.f)(Object(g.a)(z))}}]);