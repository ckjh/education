<template>
  <div>
    <header1></header1>
<!--    <right></right>-->
    <div style="height:800px; width:1600px">

      <ul>
        <video :src="videoUrl" controls="controls" style="float:left; height:450px; width:44%"></video>
      </ul>
      <hr>
      <ul>
        <reg></reg>
      </ul>

    </div>
    <footer1></footer1>
  </div>
</template>

<script>
    import header1 from '@/components/header1'
    import footer1 from '@/components/footer1'
    import right from '@/components/right'
    import reg from "./reg";

    export default {
        name: 'video',
        data() {
            return {
                videoUrl: ''
            }
        },
        mounted: function () {
            this.videoUrl = this.$route.params.video;
        },
        components: {
            header1: header1,
            footer1: footer1,
            right: right,
            reg: reg
        },
    }
</script>

<style>
</style>
