#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "phylib.h"
#include <math.h>

phylib_object *phylib_new_still_ball( unsigned char number, phylib_coord *pos ){

    // declare and initalize a new phylib object named stillBall to null, then malloc space for it
    phylib_object * stillBall = NULL;
    stillBall = malloc(sizeof(phylib_object));

    // if the malloc fails return null
    if (stillBall == NULL){
        return NULL;
    }

    // else initialize the members of a still ball structure to the appropriate values and return it
    stillBall->type = PHYLIB_STILL_BALL;
    stillBall->obj.still_ball.number = number;
    stillBall->obj.still_ball.pos.x = pos->x;
    stillBall->obj.still_ball.pos.y = pos->y;

    return stillBall;
}

phylib_object *phylib_new_rolling_ball( unsigned char number, phylib_coord *pos, phylib_coord *vel, phylib_coord *acc ){

    // declare and initalize a new phylib object named rollingBall to null, then malloc space for it
    phylib_object * rollingBall = NULL;
    rollingBall = malloc(sizeof(phylib_object));

    // if the malloc fails return null
    if (rollingBall == NULL){
        return NULL;
    }

    // else initialize the members of a rolling ball structure to the appropriate values and return it
    rollingBall->type = PHYLIB_ROLLING_BALL;
    rollingBall->obj.rolling_ball.number = number;
    rollingBall->obj.rolling_ball.pos.x = pos->x;
    rollingBall->obj.rolling_ball.pos.y = pos->y;
    rollingBall->obj.rolling_ball.vel.x = vel->x;
    rollingBall->obj.rolling_ball.vel.y = vel->y;
    rollingBall->obj.rolling_ball.acc.x = acc->x;
    rollingBall->obj.rolling_ball.acc.y = acc->y;

    return rollingBall;
}

phylib_object *phylib_new_hole( phylib_coord *pos ){

    // declare and initalize a new phylib object named theHole to null, then malloc space for it
    phylib_object * theHole = NULL;
    theHole = malloc(sizeof(phylib_object));

    // if the malloc fails return null
    if (theHole == NULL){
        return NULL;
    }

    // else initialize the members of a hole structure to the appropriate values and return it
    theHole->type = PHYLIB_HOLE;
    theHole->obj.hole.pos.x = pos->x;
    theHole->obj.hole.pos.y = pos->y;

    return theHole;
}

phylib_object *phylib_new_hcushion( double y ){

    // declare and initalize a new phylib object named theHCushion to null, then malloc space for it
    phylib_object * theHCushion = NULL;
    theHCushion = malloc(sizeof(phylib_object));

    // if the malloc fails return null
    if (theHCushion == NULL){
        return NULL;
    }

    // else initialize the members of a horizontal cushion structure to the appropriate values and return it
    theHCushion->type = PHYLIB_HCUSHION;
    theHCushion->obj.hcushion.y = y;

    return theHCushion;    
}

phylib_object *phylib_new_vcushion( double x ){

    // declare and initalize a new phylib object named theVCushion to null, then malloc space for it
    phylib_object * theVCushion = NULL;
    theVCushion = malloc(sizeof(phylib_object));

    // if the malloc fails return null
    if (theVCushion == NULL){
        return NULL;
    }

    // else initialize the members of a verticle cushion structure to the appropriate values and return it
    theVCushion->type = PHYLIB_VCUSHION;
    theVCushion->obj.vcushion.x = x;

    return theVCushion;  
}

phylib_table *phylib_new_table( void ){

    // declare and initalize a new phylib table named table to null
    phylib_table * table = NULL;

    // declare 6 holes for the table
    phylib_coord topLeft;
    phylib_coord topRight;
    phylib_coord bottomLeft;
    phylib_coord bottomRight;
    phylib_coord midRight;
    phylib_coord midLeft;

    // malloc space for the table
    table = malloc(sizeof(phylib_table));

    // if the malloc fails return null
    if (table == NULL){
        return NULL;
    }

    // else initlize the time to zero and all the compnents of the table to the appropriate values
    table->time = 0.0;
    table->object[0] = phylib_new_hcushion( 0.0 );
    table->object[1] = phylib_new_hcushion(PHYLIB_TABLE_LENGTH);
    table->object[2] = phylib_new_vcushion(0.0);
    table->object[3] = phylib_new_vcushion(PHYLIB_TABLE_WIDTH);
    topLeft.x = 0;
    topLeft.y = 0;
    table->object[4] = phylib_new_hole(&topLeft);
    midLeft.x = 0;
    midLeft.y = PHYLIB_TABLE_LENGTH/2;
    table->object[5] = phylib_new_hole(&midLeft); 
    bottomLeft.x = 0;
    bottomLeft.y = PHYLIB_TABLE_LENGTH;
    table->object[6] = phylib_new_hole(&bottomLeft);
    topRight.x = PHYLIB_TABLE_WIDTH;
    topRight.y = 0;
    table->object[7] = phylib_new_hole(&topRight); 
    midRight.x = PHYLIB_TABLE_WIDTH;
    midRight.y = PHYLIB_TABLE_LENGTH/2;
    table->object[8] = phylib_new_hole(&midRight);
    bottomRight.x = PHYLIB_TABLE_WIDTH;
    bottomRight.y = PHYLIB_TABLE_LENGTH;
    table->object[9] = phylib_new_hole(&bottomRight); 

    // the rest of the objects after the holes should be null
    for (int i = 10; i < PHYLIB_MAX_OBJECTS; i++){
        table->object[i] = NULL; 
    }

    // return this table
    return table;

}

void phylib_copy_object( phylib_object **dest, phylib_object **src ){

    // if src points to a location containing a null pointer then dest is assigned null
    if (*src == NULL){
        *dest = NULL;
    } else{

        // else allocate memory for a new object
        phylib_object * copiedObject = malloc(sizeof(phylib_object));

        // if the malloc fails return from function
        if (copiedObject == NULL){
            return;
        }

        // save the address of this object to a location pointed to by dest
        *dest = copiedObject;

        // copy the contents pointed to by src into dest
        memcpy(*dest, *src, sizeof(phylib_object));
         
    }
}

phylib_table *phylib_copy_table( phylib_table *table ){

    // if the table passed in was a null return null
    if (table == NULL){
        return NULL;
    }

    // other wise malloc space for a new table and if that malloc fails return null
    phylib_table * newTable = malloc(sizeof(phylib_table));
    if (newTable == NULL){
        return NULL;
    }

    // initalize each object inside this new table to null so its accessible
    for (int j = 0; j < PHYLIB_MAX_OBJECTS; j++){
        newTable->object[j] = NULL;
    }
  
    // go through each object of the old table and if that object isn't null copy the object into the copied table
    for (int i = 0; i < PHYLIB_MAX_OBJECTS; i++){
        if (table->object[i] != NULL){
            phylib_copy_object(&(newTable->object[i]), &(table->object[i]));
        }
    }

    // copy over the time from the old table into the new table as well
    newTable->time = table->time;

    // return this new table
    return newTable;
}

void phylib_add_object( phylib_table *table, phylib_object *object ){

    // declare and initalize an integer to keep count of the object number
    int itemNumber = 0;

    // while this object number is less than the number of max objects and the object at this number is not null
    while((itemNumber < PHYLIB_MAX_OBJECTS) && (table->object[itemNumber] != NULL)){

        // increment the itemNumber by one
        itemNumber++;
    }

    // if this number is within range add the object at this index
    if (itemNumber < PHYLIB_MAX_OBJECTS){
        table->object[itemNumber] = object;
    }
}

void phylib_free_table( phylib_table *table ){

    // if the table passed by the parameter is null return from the function
    if (table == NULL){
        return;
    }

    // declare and initalize an integer to keep count of the object number
    int objectNumber = 0;

    // while this object number is less than the number of max objects and the object at this number is not null
    while(objectNumber < PHYLIB_MAX_OBJECTS){
        if (table->object[objectNumber] != NULL){

            // free that object and increment counter
            free(table->object[objectNumber]);
            objectNumber++;
        } else{

            // else do no freeing and just increment counter
            objectNumber++;
        }
    }

    // by the end just free the table
    free(table);
}

phylib_coord phylib_sub( phylib_coord c1, phylib_coord c2 ){

    // declare a coordinate named result and update the x and y coordinates of it
    phylib_coord result;
    result.x = c1.x - c2.x;
    result.y = c1.y - c2.y;

    // return the result
    return result;
}

double phylib_length( phylib_coord c ){

    // declare a double representing the length
    double length;

    // calculate the length by the following operation and return the result
    length = sqrt(((c.x) * (c.x)) + ((c.y) * (c.y)));
    return length;
}

double phylib_dot_product( phylib_coord a, phylib_coord b ){

    // declare and initalize a variable named result that is assigned the dot product of coordinates a and b
    double result = (((a.x)*(b.x)) + ((a.y)*(b.y)));

    // return this result
    return result;
}

double phylib_distance( phylib_object *obj1, phylib_object *obj2 ){

    // declare a double initalized to -1 and declare a coordinate named result
    double distance = -1.0;
    phylib_coord result;

    // for every case the first object has to be a rolling ball and the second one either a still ball, rolling ball, a hole, verticle or horizontal cushion
    if ((obj1->type == PHYLIB_ROLLING_BALL) && ((obj2->type == PHYLIB_ROLLING_BALL) || (obj2->type == PHYLIB_STILL_BALL))){

        if (obj2->type == PHYLIB_ROLLING_BALL){

            // calculate distance between 2 rolling balls
            result = phylib_sub(obj1->obj.rolling_ball.pos, obj2->obj.rolling_ball.pos);
            distance = phylib_length(result) - PHYLIB_BALL_DIAMETER;
            return distance;
        } else{

            // calculate distance between rolling and still ball
            result = phylib_sub(obj1->obj.rolling_ball.pos, obj2->obj.still_ball.pos);
            distance = phylib_length(result) - PHYLIB_BALL_DIAMETER;
            return distance;
        }
    }
    else if ((obj1->type == PHYLIB_ROLLING_BALL) && (obj2->type == PHYLIB_HOLE)){

        // calculate distance between rolling ball and a hole
        result = phylib_sub(obj1->obj.rolling_ball.pos, obj2->obj.hole.pos);
        distance = phylib_length(result) - PHYLIB_HOLE_RADIUS;
        return distance;
    }
    else if ((obj1->type == PHYLIB_ROLLING_BALL) && ((obj2->type == PHYLIB_VCUSHION) || (obj2->type == PHYLIB_HCUSHION))){

        if (obj2->type == PHYLIB_VCUSHION){

            // calculate distance between verticle cushion and a rolling ball
            distance = obj2->obj.vcushion.x - obj1->obj.rolling_ball.pos.x;
            distance = fabs(distance) - PHYLIB_BALL_RADIUS;
            return distance;
        } else{

            // calculate distance between a horizontal cushion and a rolling ball
            distance = obj2->obj.hcushion.y - obj1->obj.rolling_ball.pos.y;
            distance = fabs(distance) - PHYLIB_BALL_RADIUS;
            return distance;
        }
    }

    // if none of those situations are true just return -1
    return distance;
}

void phylib_roll( phylib_object *new, phylib_object *old, double time ){

    // declare variables representing the old and new velocities wrt to x and y
    double oldVelX = old->obj.rolling_ball.vel.x;
    double oldVelY = old->obj.rolling_ball.vel.y;

    double newVelX, newVelY;

    // if the objects passed in are both rolling balls only then do something
    if ((new->type == PHYLIB_ROLLING_BALL) && (old->type == PHYLIB_ROLLING_BALL)){

        // update position and velocity wrt both x and y with formula given
        new->obj.rolling_ball.pos.x = old->obj.rolling_ball.pos.x + (old->obj.rolling_ball.vel.x * time) + (0.5 * (old->obj.rolling_ball.acc.x) * (time * time));
        new->obj.rolling_ball.pos.y = old->obj.rolling_ball.pos.y + (old->obj.rolling_ball.vel.y * time) + (0.5 * (old->obj.rolling_ball.acc.y) * (time * time));
        new->obj.rolling_ball.vel.x = old->obj.rolling_ball.vel.x + ((old->obj.rolling_ball.acc.x) * time);
        new->obj.rolling_ball.vel.y = old->obj.rolling_ball.vel.y + ((old->obj.rolling_ball.acc.y) * time);

        // initalize the new velocities wrt to x and y
        newVelX = new->obj.rolling_ball.vel.x;
        newVelY = new->obj.rolling_ball.vel.y;
       
        // multiply the old and new velocities together for both x and y
        oldVelX = oldVelX * newVelX;
        oldVelY =  oldVelY * newVelY;

        // if either of the x or y velicities changes signs make that corresponding acc and vel zero
        if (oldVelX < 0){
            new->obj.rolling_ball.vel.x = 0;
            new->obj.rolling_ball.acc.x = 0;
        }
        if (oldVelY < 0){
            new->obj.rolling_ball.vel.y = 0;
            new->obj.rolling_ball.acc.y = 0;
        }
    } 
}

unsigned char phylib_stopped( phylib_object *object ){ 

    // store the number, x, and y values when the ball is a rolling ball
    unsigned char number = object->obj.rolling_ball.number;
    double xValue = object->obj.rolling_ball.pos.x;
    double yValue = object->obj.rolling_ball.pos.y;

    // also declare a double named speed that is computed using the length function
    double speed = phylib_length(object->obj.rolling_ball.vel);

    // if this speed is less than velocity epsilon
    if (speed < PHYLIB_VEL_EPSILON){

        // convert the rolling ball to a still ball indicating it has stopped
        object->type = PHYLIB_STILL_BALL;

        // using the values stores prevously when the ball was a rolling ball, assign them to the corresponding members of a still ball
        object->obj.still_ball.number = number;
        object->obj.still_ball.pos.x = xValue;
        object->obj.still_ball.pos.y = yValue;

        return 1;
    }

    return 0;
}

void phylib_bounce( phylib_object **a, phylib_object **b ){

    // declare variables that need to be computed in the following cases
    unsigned char number;
    double xValue;
    double yValue;
    phylib_coord r_ab;
    r_ab.x = 0;
    r_ab.y = 0;
    phylib_coord v_rel;
    v_rel.x = 0;
    v_rel.y = 0;
    phylib_coord n;
    n.x = 0;
    n.y = 0;
    double v_rel_n = 0;
    double lengthX = 0;
    double lengthY = 0;
    double speedA = 0;
    double speedB = 0;
    switch((*b)->type){
        case 3:

            // if b is a horizontal cushion negate the y acc and y vel of *a
            (*a)->obj.rolling_ball.vel.y = ((*a)->obj.rolling_ball.vel.y) * (-1);
            (*a)->obj.rolling_ball.acc.y = ((*a)->obj.rolling_ball.acc.y) * (-1);
            break;
        case 4:

            // if b is a verticle cushion negate the x acc and x vel of *a
            (*a)->obj.rolling_ball.vel.x = ((*a)->obj.rolling_ball.vel.x) * (-1);
            (*a)->obj.rolling_ball.acc.x = ((*a)->obj.rolling_ball.acc.x) * (-1);
            break;
        case 2:

            // if b is a hole free the rolling ball and set it to null
            free((*a));
            (*a) = NULL; // ball falling into the table
            break;
        case 0:

            // if b is a still ball convert it to a rolling ball ensuring to copy over the still ball members' values and setting vel and acc to 0
            number = (*b)->obj.still_ball.number;
            xValue = (*b)->obj.still_ball.pos.x;
            yValue = (*b)->obj.still_ball.pos.y;
            (*b)->type = PHYLIB_ROLLING_BALL;
            (*b)->obj.rolling_ball.number = number;
            (*b)->obj.rolling_ball.pos.x = xValue;
            (*b)->obj.rolling_ball.pos.y = yValue;
            (*b)->obj.rolling_ball.vel.x = 0.0;
            (*b)->obj.rolling_ball.vel.y = 0.0;
            (*b)->obj.rolling_ball.acc.x = 0.0;
            (*b)->obj.rolling_ball.acc.y = 0.0;
        case 1:

            // if b is a rolling ball compute position of a wrt b
            r_ab = phylib_sub( (*a)->obj.rolling_ball.pos, (*b)->obj.rolling_ball.pos );

            // compute velocity of a wrt b
            v_rel = phylib_sub((*a)->obj.rolling_ball.vel, (*b)->obj.rolling_ball.vel);

            // compute the normal vector
            lengthX = r_ab.x/phylib_length(r_ab);
            lengthY = r_ab.y/phylib_length(r_ab);
            n.x = lengthX;
            n.y = lengthY;

            // compute the relative velocity
            v_rel_n = phylib_dot_product(v_rel, n);

            // update x and y velocities of both a and b
            (*a)->obj.rolling_ball.vel.x = ((*a)->obj.rolling_ball.vel.x) - (v_rel_n * n.x);
            (*a)->obj.rolling_ball.vel.y = ((*a)->obj.rolling_ball.vel.y) - (v_rel_n * n.y);

            (*b)->obj.rolling_ball.vel.x = ((*b)->obj.rolling_ball.vel.x) + (v_rel_n * n.x);
            (*b)->obj.rolling_ball.vel.y = ((*b)->obj.rolling_ball.vel.y) + (v_rel_n * n.y);

            // compute the speed of both a and b
            speedA = phylib_length((*a)->obj.rolling_ball.vel);
            speedB = phylib_length((*b)->obj.rolling_ball.vel);


            // if either speed is less than the velocity epsilon update the x and y accelertation of that object
            if (speedA > PHYLIB_VEL_EPSILON){

                (*a)->obj.rolling_ball.acc.x = (-1)*((*a)->obj.rolling_ball.vel.x/(speedA) * PHYLIB_DRAG);
                (*a)->obj.rolling_ball.acc.y = (-1)*((*a)->obj.rolling_ball.vel.y/(speedA) * PHYLIB_DRAG);
            }

            if (speedB > PHYLIB_VEL_EPSILON){

                (*b)->obj.rolling_ball.acc.x = (-1)*((*b)->obj.rolling_ball.vel.x/(speedB) * PHYLIB_DRAG);
                (*b)->obj.rolling_ball.acc.y = (-1)*((*b)->obj.rolling_ball.vel.y/(speedB) * PHYLIB_DRAG);
            }
            break;
    }
   
}

unsigned char phylib_rolling( phylib_table *t ){

    // declare a variable for a counter
    unsigned char counter = 0;

    // go through each object on the table and check if that object is null
    for (int i = 0; i < PHYLIB_MAX_OBJECTS; i++){

        if (t->object[i] != NULL){

            // if it is not null check if it's a rolling ball
            if (t->object[i]->type == PHYLIB_ROLLING_BALL){

                // if it is add one to the counter
                counter++;
            }
        }
    }

    // at the end return the counter
    return counter;
}


phylib_table *phylib_segment( phylib_table *table ){

    // set the time to the phylib_sim_rate
    double time = PHYLIB_SIM_RATE;

    // get the number of rolling balls using the rolling function
    unsigned char rollingBalls = phylib_rolling(table);

    // declare and initailze doubles representing if a ball has stopped and the result for the distance
    double stopped = 0;
    double result = 0;

    // if there are no rolling balls return null
    if(rollingBalls == 0){
        return NULL;
    }

    // if the table passed is null return null
    if (table == NULL){
        return NULL;
    }

    // declare and initalize a variable names copiedtable using the copy table function
    phylib_table * copiedTable =  phylib_copy_table(table);

    // keep going until max time is reached (case 1)
    while (time < PHYLIB_MAX_TIME){

        // go through each object and if the object is a rolling ball apply the phylib roll function to that object
        for (int i = 0; i < PHYLIB_MAX_OBJECTS; i++){
            if (copiedTable->object[i] != NULL){
                if (copiedTable->object[i]->type == PHYLIB_ROLLING_BALL){
                    phylib_roll( copiedTable->object[i], table->object[i], time);
                }
            }
        }

        // go through each object and do that again so objects are comparable (case 2)
        for (int k = 0; k < PHYLIB_MAX_OBJECTS; k++){
            for (int j = 0; j < PHYLIB_MAX_OBJECTS; j++){

                // if both objects are not null and the first object is a rolling ball and the objects indexes do not equal one another
                if ((copiedTable->object[k] != NULL) && (copiedTable->object[j] != NULL)){
                    if ((copiedTable->object[k]->type == PHYLIB_ROLLING_BALL) && (k != j)){

                        // caclulate the distance between a rolling ball and the second object
                        result = phylib_distance( copiedTable->object[k], copiedTable->object[j]);

                        // if the distance is less than 0.0 apply the bounce function the ball and object
                        if (result <= 0.0){

                            phylib_bounce( &(copiedTable->object[k]), &(copiedTable->object[j]));

                            // update the time before returning the table
                            copiedTable->time = copiedTable->time + time;

                            // return copied table
                            return copiedTable;
                        }
                    }
                }
            }
            
        }

        // go through each object in the table to check if the rolling ball has stopped (case 3)
        for(int m = 0; m < PHYLIB_MAX_OBJECTS; m++){
            if ((copiedTable->object[m] != NULL) && (copiedTable->object[m]->type == PHYLIB_ROLLING_BALL)){
                stopped = phylib_stopped( copiedTable->object[m] );
                if (stopped == 1){
                    copiedTable->time = copiedTable->time + time;
                    return copiedTable;
                }

            }
        }
        
        // increment time by the sim rate
        time = time + PHYLIB_SIM_RATE;
    }
  
    // if the time has maxed out update the time to the copied table and return the copied table
    copiedTable->time = copiedTable->time + time;
    return copiedTable;
}

// new function added
char *phylib_object_string( phylib_object *object )
{
    static char string[80];
    if (object==NULL)
    {
        sprintf( string, "NULL;" );
        return string;
    }
    switch (object->type)
    {
        case PHYLIB_STILL_BALL:
            sprintf( string,
            "STILL_BALL (%d,%6.1lf,%6.1lf)",
            object->obj.still_ball.number,
            object->obj.still_ball.pos.x,
            object->obj.still_ball.pos.y );
            break;
        case PHYLIB_ROLLING_BALL:
            sprintf( string,
            "ROLLING_BALL (%d,%6.1lf,%6.1lf,%6.1lf,%6.1lf,%6.1lf,%6.1lf)",
            object->obj.rolling_ball.number,
            object->obj.rolling_ball.pos.x,
            object->obj.rolling_ball.pos.y,
            object->obj.rolling_ball.vel.x,
            object->obj.rolling_ball.vel.y,
            object->obj.rolling_ball.acc.x,
            object->obj.rolling_ball.acc.y );
            break;
        case PHYLIB_HOLE:
            sprintf( string,
            "HOLE (%6.1lf,%6.1lf)",
            object->obj.hole.pos.x,
            object->obj.hole.pos.y );
            break;
        case PHYLIB_HCUSHION:
            sprintf( string,
            "HCUSHION (%6.1lf)",
            object->obj.hcushion.y );
            break;
        case PHYLIB_VCUSHION:
            sprintf( string,
            "VCUSHION (%6.1lf)",
            object->obj.vcushion.x );
            break;
    }
    return string;
    }