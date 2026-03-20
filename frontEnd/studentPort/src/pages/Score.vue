<script>
    export default {
        data(){
            return{
                studentId:"",
                semester:""
            }
        }
    }
</script>

<template>

    <div>

        <h2>คะแนน</h2>

        <input placeholder="ปีการศึกษา">
        <input placeholder="ภาคเรียน">

        <table>
            <tr>
                <th>วิชา</th>
                <th>คะแนน</th>
            </tr>

            <tr>
                <td>Programming</td>
                <td>85</td>
            </tr>
        </table>

    </div>

</template>