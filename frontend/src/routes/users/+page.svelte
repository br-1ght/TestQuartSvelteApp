<script>
    import {onMount} from "svelte"

    export let data
    let users = data.users
    let errors = data.errors

</script>

{#if errors}
   <p class="text-danger">{errors}</p> 
{:else}
   <table class="table">
       <thead>
           <tr>
               <th scope="col">ID</th>
               <th scope="col">Name</th>
           </tr>
       </thead>
       <tbody>
           {#each users as user }
               <tr>
                   <td>{user.id}</td>
                   <td>{user.name}</td>
               </tr> 
           {/each}
       </tbody>
   </table>
{/if}