import { InertiaApp } from '@inertiajs/inertia-vue'
import Vue from 'vue'
import axios from "axios";
import PortalVue from 'portal-vue'


axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

Vue.config.productionTip = false;

Vue.use(InertiaApp);
Vue.use(PortalVue);

window.route = function(url_name) {
  
 return window.reverseUrl("demo:"+url_name);
  
}

Vue.mixin({ methods: { route: window.route } });

const app = document.getElementById('app');
// we are getting the initialPage from a rendered json_script
const page = JSON.parse(document.getElementById("page").textContent);

import Index from "./Pages/Index";

const pages = {
  'Index': Index
}
new Vue({
  render: h => h(InertiaApp, {
    props: {
      initialPage: page,
      resolveComponent: (name) => {
        return pages[name];
      },
    },
  }),
}).$mount(app)