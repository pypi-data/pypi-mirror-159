(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[12],{1379:function(e,t,n){var r=n(1380);e.exports=function(e,t){return!!(null==e?0:e.length)&&r(e,t,0)>-1}},1380:function(e,t,n){var r=n(1381),o=n(1382),i=n(1383);e.exports=function(e,t,n){return t===t?i(e,t,n):r(e,o,n)}},1381:function(e,t){e.exports=function(e,t,n,r){for(var o=e.length,i=n+(r?1:-1);r?i--:++i<o;)if(t(e[i],i,e))return i;return-1}},1382:function(e,t){e.exports=function(e){return e!==e}},1383:function(e,t){e.exports=function(e,t,n){for(var r=n-1,o=e.length;++r<o;)if(e[r]===t)return r;return-1}},1384:function(e,t){e.exports=function(e,t,n){for(var r=-1,o=null==e?0:e.length;++r<o;)if(n(t,e[r]))return!0;return!1}},1713:function(e,t,n){var r=n(1714),o=n(512),i=n(511),a=o((function(e,t){return i(e)?r(e,t):[]}));e.exports=a},1714:function(e,t,n){var r=n(507),o=n(1379),i=n(1384),a=n(339),u=n(263),l=n(508);e.exports=function(e,t,n,s){var c=-1,p=o,d=!0,f=e.length,m=[],h=t.length;if(!f)return m;n&&(t=a(t,u(n))),s?(p=i,d=!1):t.length>=200&&(p=l,d=!1,t=new r(t));e:for(;++c<f;){var v=e[c],g=null==n?v:n(v);if(v=s||0!==v?v:0,d&&g===g){for(var b=h;b--;)if(t[b]===g)continue e;m.push(v)}else p(t,g,s)||m.push(v)}return m}},1821:function(e,t,n){"use strict";n.r(t),n.d(t,"default",(function(){return O}));var r=n(2),o=n(4),i=n(6),a=n(7),u=n(0),l=n.n(u),s=n(1713),c=n.n(s),p=n(74),d=n(211),f=n(1164),m=n(78),h=n(128),v=n(10),g=Object(v.a)("div",{target:"ede6r8z0"})((function(e){return{"span[aria-disabled='true']":{background:e.theme.colors.fadedText05}}}),""),b=n(129),y=n(65),x=n(166),w=n(336),j=n(1),S=function(e){Object(i.a)(n,e);var t=Object(a.a)(n);function n(){var e;Object(r.a)(this,n);for(var o=arguments.length,i=new Array(o),a=0;a<o;a++)i[a]=arguments[a];return(e=t.call.apply(t,[this].concat(i))).formClearHelper=new d.b,e.state={value:e.initialValue},e.commitWidgetValue=function(t){e.props.widgetMgr.setIntArrayValue(e.props.element,e.state.value,t)},e.onFormCleared=function(){e.setState({value:e.props.element.default},(function(){return e.commitWidgetValue({fromUi:!0})}))},e.onChange=function(t){var n=e.generateNewState(t);e.setState(n,(function(){return e.commitWidgetValue({fromUi:!0})}))},e.filterOptions=function(t,n){var r=t.filter((function(t){return!e.state.value.includes(Number(t.value))}));return Object(w.b)(r,n)},e}return Object(o.a)(n,[{key:"initialValue",get:function(){var e=this.props.widgetMgr.getIntArrayValue(this.props.element);return void 0!==e?e:this.props.element.default}},{key:"componentDidMount",value:function(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}},{key:"componentDidUpdate",value:function(){this.maybeUpdateFromProtobuf()}},{key:"componentWillUnmount",value:function(){this.formClearHelper.disconnect()}},{key:"maybeUpdateFromProtobuf",value:function(){this.props.element.setValue&&this.updateFromProtobuf()}},{key:"updateFromProtobuf",value:function(){var e=this,t=this.props.element.value;this.props.element.setValue=!1,this.setState({value:t},(function(){e.commitWidgetValue({fromUi:!1})}))}},{key:"valueFromState",get:function(){var e=this;return this.state.value.map((function(t){var n=e.props.element.options[t];return{value:t.toString(),label:n}}))}},{key:"generateNewState",value:function(e){var t=function(){var t,n=null===(t=e.option)||void 0===t?void 0:t.value;return parseInt(n,10)};switch(e.type){case"remove":return{value:c()(this.state.value,t())};case"clear":return{value:[]};case"select":return{value:this.state.value.concat([t()])};default:throw new Error("State transition is unknown: ".concat(e.type))}}},{key:"render",value:function(){var e=this.props,t=e.element,n=e.theme,r=e.width,o=e.widgetMgr,i={width:r},a=t.options,u=0===a.length||this.props.disabled,l=0===a.length?"No options to select.":"Choose an option",s=a.map((function(e,t){return{label:e,value:t.toString()}}));return this.formClearHelper.manageFormClearListener(o,t.formId,this.onFormCleared),Object(j.jsxs)("div",{className:"row-widget stMultiSelect",style:i,children:[Object(j.jsx)(h.d,{label:t.label,disabled:u,children:t.help&&Object(j.jsx)(h.b,{children:Object(j.jsx)(b.a,{content:t.help,placement:y.b.TOP_RIGHT})})}),Object(j.jsx)(g,{children:Object(j.jsx)(f.a,{options:s,labelKey:"label",valueKey:"value",placeholder:l,type:m.b.select,multi:!0,onChange:this.onChange,value:this.valueFromState,disabled:u,size:"compact",filterOptions:this.filterOptions,overrides:{IconsContainer:{style:function(){return{paddingRight:".5rem"}}},ControlContainer:{style:function(){return{borderLeftWidth:"1px",borderRightWidth:"1px",borderTopWidth:"1px",borderBottomWidth:"1px"}}},ValueContainer:{style:function(){return{minHeight:"40px",paddingLeft:".5rem"}}},ClearIcon:{style:{color:n.colors.darkGray}},SearchIcon:{style:{color:n.colors.darkGray}},Tag:{props:{overrides:{Root:{style:{borderTopLeftRadius:n.radii.md,borderTopRightRadius:n.radii.md,borderBottomRightRadius:n.radii.md,borderBottomLeftRadius:n.radii.md,fontSize:n.fontSizes.sm,paddingLeft:n.spacing.sm,marginLeft:0,marginRight:n.spacing.sm,height:"28px"}},Action:{style:{paddingLeft:0}},Text:{style:{fontSize:n.fontSizes.md}}}}},MultiValue:{props:{overrides:{Root:{style:{fontSize:n.fontSizes.sm}}}}},Dropdown:{component:x.a}}})})]})}}]),n}(l.a.PureComponent),O=Object(p.f)(S)}}]);