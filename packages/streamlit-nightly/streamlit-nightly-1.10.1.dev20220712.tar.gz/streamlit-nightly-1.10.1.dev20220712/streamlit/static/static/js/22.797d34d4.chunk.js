(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[22],{1325:function(e,t,n){"use strict";n(0);var r,o=n(49),a=n(128),i=n(5),u=n(156),c=n(10),l=n(52),s=Object(l.c)(r||(r=Object(u.a)(["\n  50% {\n    color: rgba(0, 0, 0, 0);\n  }\n"]))),p=Object(c.a)("span",{target:"e1m4n6jn0"})((function(e){var t=e.includeDot,n=e.shouldBlink,r=e.theme;return Object(i.a)(Object(i.a)({},t?{"&::before":{opacity:1,content:'"\u2022"',animation:"none",color:r.colors.gray,margin:"0 5px"}}:{}),n?{color:r.colors.red,animationName:"".concat(s),animationDuration:"0.5s",animationIterationCount:5}:{})}),""),f=n(1);t.a=function(e){var t=e.dirty,n=e.value,r=e.maxLength,i=e.className,u=e.type,c=[],l=function(e){var t=arguments.length>1&&void 0!==arguments[1]&&arguments[1];c.push(Object(f.jsx)(p,{includeDot:c.length>0,shouldBlink:t,children:e},c.length))};return t&&("multiline"===(void 0===u?"single":u)?Object(o.f)()?l("Press \u2318+Enter to apply"):l("Press Ctrl+Enter to apply"):l("Press Enter to apply")),r&&l("".concat(n.length,"/").concat(r),t&&n.length>=r),Object(f.jsx)(a.a,{className:i,children:c})}},1426:function(e,t,n){"use strict";var r=n(0),o=n(18),a=n(1360),i=n(1432),u=n(1300),c=n(100);function l(e){return(l="function"===typeof Symbol&&"symbol"===typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"===typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function s(){return(s=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e}).apply(this,arguments)}function p(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if(!(Symbol.iterator in Object(e))&&"[object Arguments]"!==Object.prototype.toString.call(e))return;var n=[],r=!0,o=!1,a=void 0;try{for(var i,u=e[Symbol.iterator]();!(r=(i=u.next()).done)&&(n.push(i.value),!t||n.length!==t);r=!0);}catch(c){o=!0,a=c}finally{try{r||null==u.return||u.return()}finally{if(o)throw a}}return n}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}function f(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},a=Object.keys(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}function d(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function h(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}function m(e,t){return!t||"object"!==l(t)&&"function"!==typeof t?y(e):t}function b(e){return(b=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function y(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function g(e,t){return(g=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e})(e,t)}function v(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}var j=function(e){function t(){var e,n;d(this,t);for(var r=arguments.length,o=new Array(r),a=0;a<r;a++)o[a]=arguments[a];return v(y(n=m(this,(e=b(t)).call.apply(e,[this].concat(o)))),"state",{isFocused:n.props.autoFocus||!1}),v(y(n),"onFocus",(function(e){n.setState({isFocused:!0}),n.props.onFocus(e)})),v(y(n),"onBlur",(function(e){n.setState({isFocused:!1}),n.props.onBlur(e)})),n}var n,l,j;return function(e,t){if("function"!==typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&g(e,t)}(t,e),n=t,(l=[{key:"render",value:function(){var e=this.props,t=e.startEnhancer,n=e.endEnhancer,l=e.overrides,d=l.Root,h=l.StartEnhancer,m=l.EndEnhancer,b=f(l,["Root","StartEnhancer","EndEnhancer"]),y=f(e,["startEnhancer","endEnhancer","overrides"]),g=p(Object(o.c)(d,u.d),2),v=g[0],j=g[1],w=p(Object(o.c)(h,u.c),2),S=w[0],E=w[1],x=p(Object(o.c)(m,u.c),2),P=x[0],C=x[1],F=Object(a.a)(this.props,this.state);return r.createElement(v,s({"data-baseweb":"input"},F,j,{$adjoined:O(t,n),$hasIconTrailing:this.props.clearable||"password"==this.props.type}),t&&r.createElement(S,s({},F,E,{$position:c.c.start}),"function"===typeof t?t(F):t),r.createElement(i.a,s({},y,{overrides:b,adjoined:O(t,n),onFocus:this.onFocus,onBlur:this.onBlur})),n&&r.createElement(P,s({},F,C,{$position:c.c.end}),"function"===typeof n?n(F):n))}}])&&h(n.prototype,l),j&&h(n,j),t}(r.Component);function O(e,t){return e&&t?c.a.both:e?c.a.left:t?c.a.right:c.a.none}v(j,"defaultProps",{autoComplete:"on",autoFocus:!1,disabled:!1,name:"",error:!1,onBlur:function(){},onFocus:function(){},overrides:{},required:!1,size:c.d.default,startEnhancer:null,endEnhancer:null,clearable:!1,type:"text"}),t.a=j},1824:function(e,t,n){"use strict";n.r(t),n.d(t,"default",(function(){return j}));var r=n(2),o=n(4),a=n(6),i=n(7),u=n(0),c=n.n(u),l=n(1426),s=n(23),p=n(211),f=n(1325),d=n(128),h=n(129),m=n(65),b=n(49),y=n(10),g=Object(y.a)("div",{target:"edfmue0"})((function(e){e.theme;return{position:"relative",width:e.width}}),""),v=n(1),j=function(e){Object(a.a)(n,e);var t=Object(i.a)(n);function n(){var e;Object(r.a)(this,n);for(var o=arguments.length,a=new Array(o),i=0;i<o;i++)a[i]=arguments[i];return(e=t.call.apply(t,[this].concat(a))).formClearHelper=new p.b,e.state={dirty:!1,value:e.initialValue},e.commitWidgetValue=function(t){e.props.widgetMgr.setStringValue(e.props.element,e.state.value,t),e.setState({dirty:!1})},e.onFormCleared=function(){e.setState({value:e.props.element.default},(function(){return e.commitWidgetValue({fromUi:!0})}))},e.onBlur=function(){e.state.dirty&&e.commitWidgetValue({fromUi:!0})},e.onChange=function(t){var n=t.target.value,r=e.props.element.maxChars;0!==r&&n.length>r||(Object(b.h)(e.props.element)?e.setState({dirty:!1,value:n},(function(){return e.commitWidgetValue({fromUi:!0})})):e.setState({dirty:!0,value:n}))},e.onKeyPress=function(t){"Enter"===t.key&&e.state.dirty&&e.commitWidgetValue({fromUi:!0})},e}return Object(o.a)(n,[{key:"initialValue",get:function(){var e=this.props.widgetMgr.getStringValue(this.props.element);return void 0!==e?e:this.props.element.default}},{key:"componentDidMount",value:function(){this.props.element.setValue?this.updateFromProtobuf():this.commitWidgetValue({fromUi:!1})}},{key:"componentDidUpdate",value:function(){this.maybeUpdateFromProtobuf()}},{key:"componentWillUnmount",value:function(){this.formClearHelper.disconnect()}},{key:"maybeUpdateFromProtobuf",value:function(){this.props.element.setValue&&this.updateFromProtobuf()}},{key:"updateFromProtobuf",value:function(){var e=this,t=this.props.element.value;this.props.element.setValue=!1,this.setState({value:t},(function(){e.commitWidgetValue({fromUi:!1})}))}},{key:"getTypeString",value:function(){return this.props.element.type===s.s.Type.PASSWORD?"password":"text"}},{key:"render",value:function(){var e=this.state,t=e.dirty,n=e.value,r=this.props,o=r.element,a=r.width,i=r.disabled,u=r.widgetMgr,c=o.placeholder;return this.formClearHelper.manageFormClearListener(u,o.formId,this.onFormCleared),Object(v.jsxs)(g,{className:"row-widget stTextInput",width:a,children:[Object(v.jsx)(d.d,{label:o.label,disabled:i,children:o.help&&Object(v.jsx)(d.b,{children:Object(v.jsx)(h.a,{content:o.help,placement:m.b.TOP_RIGHT})})}),Object(v.jsx)(l.a,{value:n,placeholder:c,onBlur:this.onBlur,onChange:this.onChange,onKeyPress:this.onKeyPress,disabled:i,type:this.getTypeString(),autoComplete:o.autocomplete,overrides:{Input:{style:{minWidth:0,"::placeholder":{opacity:"0.7"},lineHeight:"1.4",paddingRight:".5rem",paddingLeft:".5rem",paddingBottom:".5rem",paddingTop:".5rem"}},Root:{style:{borderLeftWidth:"1px",borderRightWidth:"1px",borderTopWidth:"1px",borderBottomWidth:"1px"}}}}),Object(v.jsx)(f.a,{dirty:t,value:n,maxLength:o.maxChars})]})}}]),n}(c.a.PureComponent)}}]);