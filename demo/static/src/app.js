import { InertiaApp } from '@inertiajs/inertia-vue'
import Vue from 'vue'
import axios from "axios";
import PortalVue from 'portal-vue'


axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

Vue.config.productionTip = false;

Vue.use(InertiaApp);
Vue.use(PortalVue);

Vue.mixin({ methods: { route: window.reverseUrl } });

const app = document.getElementById('app');
// we are getting the initialPage from a rendered json_script
const page = JSON.parse(document.getElementById("page").textContent);

import Index from "./Pages/Index";
import Contacts from "./Pages/Contacts";
import Organization from "./Pages/Organizations";
import ContactEdit from "./Pages/Contacts.Edit";

const pages = {
  'Index': Index,
  'Contacts': Contacts,
  'Organization': Organization,
  'Contacts.Edit': ContactEdit,
}


new Vue({
  render: h => h(InertiaApp, {
    props: {
      initialPage: page,
      resolveComponent: (name) => {
        console.log("resolveComponent ", name)
        return pages[name];
      },
    },
  }),
}).$mount(app)
