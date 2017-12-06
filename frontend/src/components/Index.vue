<template>
  <div>
    <x-header :right-options="{showMore: true}" :left-optins="{showBack:false}" @on-click-more="showMenus = true" @on-click-back="back()">Index</x-header>
    <box gap="10px 10px">
      <flexbox>
        <flexbox-item>
          <x-button type="primary" @click.native="get">primary</x-button>
        </flexbox-item>
      </flexbox>
    </box>
    <tabbar>
      <tabbar-item>
        <img slot="icon" src="../assets/icon_nav_button.png">
        <span slot="label">Wechat</span>
      </tabbar-item>
      <tabbar-item show-dot>
        <img slot="icon" src="../assets/icon_nav_msg.png">
        <span slot="label">Message</span>
      </tabbar-item>
      <tabbar-item selected link="/component/demo">
        <img slot="icon" src="../assets/icon_nav_article.png">
        <span slot="label">Explore</span>
      </tabbar-item>
      <tabbar-item badge="2">
        <img slot="icon" src="../assets/icon_nav_cell.png">
        <span slot="label">News</span>
      </tabbar-item>
    </tabbar>
  </div>
</template>

<script>
  import Vue from 'vue'
  import { XHeader, XButton, Box, GroupTitle, Flexbox, FlexboxItem, Divider, Tabbar, TabbarItem, Group, Cell, ToastPlugin } from 'vux'
  Vue.use(ToastPlugin)
  export default {
    components: {
      XHeader,
      XButton,
      Box,
      GroupTitle,
      Group,
      Flexbox,
      FlexboxItem,
      Divider,
      Tabbar,
      TabbarItem,
      Cell
    },
    data () {
      return {
        showMenus: false,
        user: {}
      }
    },
    methods: {
      back: function () {
        this.$router.go(0)
      },
      get: function () {
        let $this = this
        let url = '/show_user'
        $this.axios.get(url)
        .then(function (response) {
          response = response.data
          if (response.status === 200) {
            $this.$vux.toast.show({
              type: 'success',
              text: 'success'
            })
            $this.user = response.list
            console.log($this.user)
          } else {
            $this.$vux.toast.show({
              type: 'warn',
              text: 'error'
            })
          }
        })
        .catch(function (error) {
          console.log(error)
        })
      }
    }
  }
</script>

<style>
  .overwrite-title-demo {
    margin-top: 5px;
  }
</style>
