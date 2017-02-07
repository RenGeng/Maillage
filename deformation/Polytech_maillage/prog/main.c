#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <time.h>
#include "libmesh5.h"
#include "mesh.h"
#include "InOut.h"
#include <time.h>



/* parse command line arguments (not used) */
static int parsar(int argc,char *argv[],pMesh mesh) {
	int     i;
	char   *ptr;

	i = 1;
	while ( i < argc ) {
		if ( mesh->namein == NULL ) {
			mesh->namein = (char*) calloc(strlen(argv[i])+1,sizeof(char));
    		strcpy(mesh->namein,argv[i]);
		}
	    else if ( mesh->nameout == NULL ){
			mesh->nameout = (char*) calloc(strlen(argv[i])+1,sizeof(char));
    		strcpy(mesh->nameout,argv[i]);
    	}
    	i++;
	}

	/* check file names */
	if ( mesh->namein == NULL ) {
		mesh->namein = (char *)calloc(128,sizeof(char));
		assert(mesh->namein);
	    fprintf(stdout,"  -- INPUT MESH NAME ?\n");
		fflush(stdin);
	    fscanf(stdin,"%s",mesh->namein);
	}

	if ( mesh->nameout == NULL ) {
	    mesh->nameout = (char *)calloc(128,sizeof(char));
	    assert(mesh->nameout);
	    strcpy(mesh->nameout,mesh->namein);
	    ptr = strstr(mesh->nameout,".mesh");
	
	    if ( ptr ) *ptr = '\0';
	
	    strcat(mesh->nameout,".o.mesh");
	    ptr = strstr(mesh->nameout,".meshb");
	
	    if ( ptr )  strcat(mesh->nameout,"b");
	}

	return(1);
}

 

int main(int argc,char *argv[]) {
	
		
    Mesh	mesh;
  
		/* default values */
		memset(&mesh,0,sizeof(Mesh));
		
		/* parse arguments */
		fprintf(stdout,"\n  -- DATA MESH\n");
  		if ( !parsar(argc,argv,&mesh) )  return(1);
  	
      /* read data */
  		fprintf(stdout,"\n  -- INPUT DATA MESH \n");
		if ( !loadMesh(&mesh) )  return(1);
		fprintf(stdout,"  -- DATA READING COMPLETED.\n");
		
		
		/* save mesh */
		fprintf(stdout,"\n  -- OUTPUT DATA\n");
  		if ( !saveMesh(&mesh) )  return(1);
  		fprintf(stdout,"  -- WRITING COMPLETED\n The new mesh created is a (name).o.mesh \n ");	

	
	


	return(0);
}


