<template>
    <div id="index">
        <form class="layui-form sel">
            <div class="layui-form-item">
                <select lay-search >
                    <option value="">请输入车站</option>
                    <option  v-for="item in stations" :value="item" >{{item}}</option>
                </select>
            </div>
            <a :href="URL"><button type="button" @click="Search" class="layui-btn self_btn">查询</button></a>
        </form>
    </div>
</template>

<script>
    import Bus from './Bus'
    var sele = "";
    export default {
        name: "index",
        data(){
            return{
                station:"",
                stations:[],
                URL:""
            }
        },
        mounted(){
            this.$http.get("http://127.0.0.1:8000/api/stations").then(res=>{
                this.stations = res.body;
            })
        },
        methods:{
            Search(){
                Bus.$emit("City",sele);
                this.URL = "/result?C="+sele+"";
            }
        }
    }
    layui.use('form', function(){
        var form = layui.form;
        form.on('select()', function(data){
        // console.log(data.elem); //得到select原始DOM对象
        console.log(data.value); //得到被选中的值
        sele = data.value;
        // console.log(data.othis); //得到美化后的DOM对象
        });
    });
</script>

<style>
    #index{
        margin-top: 60px;
    }
    .sel{
        width: 350px;
        margin-left: 5px;
    }
    .layui-edge{
        display: none;
    }
    .self_btn{
        margin-top: 20px;
        width: 100%;
    }
</style>