<script>
    export default{
        props:["text"]
    }
</script>

<template>
    <div class="header">
        {{ text }}
    </div>
</template>

<style>
.header{
 font-weight:bold;
 background:#ddd;
 padding:12px;
 border-radius:8px;
}
</style>